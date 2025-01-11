from datasets import load_dataset
import os
from huggingface_hub import InferenceClient
import json
import asyncio


# CONFIG
os.environ["HF_TOKEN"] = "..."  # specify your token
MAX_CONCURRENT_REQUESTS = 12
CHUNK_SIZE = 1000
DATASET_NAME = "anakin87/FineTome-single-turn-dedup"
TRANSLATED_DATASET_NAME = "anakin87/FineTome-single-turn-dedup-ita"
OUTPUT_FILE = "instructions_ita.json"


fast_client = InferenceClient("meta-llama/Meta-Llama-3.1-70B-Instruct", timeout=90)
slow_client = InferenceClient("meta-llama/Meta-Llama-3.1-70B-Instruct", timeout=180)

response_format = {
    "type": "json",
    "value": {
        "properties": {
            "traduzione": {"type": "string"},
        },
        "required": ["traduzione"],
    },
}


def translate(text, client):
    """Translate text in Italian using Llama-3.1-70B-Instruct."""

    prompt = """Traduci in italiano il seguente testo.
Istruzioni:
1. L'output deve essere un JSON con il testo tradotto nella chiave "traduzione".
2. è importante che il testo sia corretto, fluido e coerente in italiano.
Testo da tradurre:
"""

    messages = [{"role": "user", "content": f"{prompt}{text}"}]

    rsp = client.chat_completion(
        messages, response_format=response_format, temperature=0.8, max_tokens=3000
    )

    traduzione = None
    try:
        traduzione = json.loads(rsp.choices[0].message.content)["traduzione"]
    except:
        pass

    return traduzione


def translate_instructions_from_row(row):
    """Translate system and user message from a row of the dataset."""

    translations = []

    for msg in row["conversations"]:
        if msg["role"] not in ["system", "user"]:
            continue

        try:
            translated_content = translate(msg["content"], fast_client)
        except:
            translated_content = translate(msg["content"], slow_client)

        if translated_content is None:
            return None

        if translated_content:
            translations.append({"content": translated_content, "role": msg["role"]})

    new_row = {"conversations": row["conversations"],
               "conversations_it": translations,
              "id": row["id"],
              "source": row["source"]}
    
    return new_row


async def translate_concurrently(example, semaphore):
    async with semaphore:
        try:
            return await asyncio.to_thread(translate_instructions_from_row, example)
        except Exception as e:
            print(f"Translation failed for example {example['id']}: {e}")
            return None


async def concrun(data):
    semaphore = asyncio.Semaphore(MAX_CONCURRENT_REQUESTS)

    tasks = [translate_concurrently(example, semaphore) for example in data]
    total_tasks = len(tasks)
    completed_tasks = 0

    # Create a progress monitor coroutine
    async def progress_monitor():
        nonlocal completed_tasks
        while completed_tasks < total_tasks:
            print(f"Completed {completed_tasks}/{total_tasks} translations")
            await asyncio.sleep(30)

    # Run the progress monitor and translation tasks concurrently
    progress_task = asyncio.create_task(progress_monitor())
    for task in asyncio.as_completed(tasks):
        translated_text = await task
        completed_tasks += 1

        if translated_text is None:
            print("Translation failed")
            continue

        try:
            serialized = json.dumps(translated_text)
        except:
            print("JSON error")

        # Append the result to the JSON Lines file
        with open("instructions_ita.json", "a+") as f:
            f.write("\n" + serialized)

    # Ensure the progress monitor completes
    await progress_task


if __name__ == "__main__":
    english_dataset = load_dataset(DATASET_NAME, split="train")
    # add id column
    english_dataset = english_dataset.add_column("id", [str(i) for i in range(len(english_dataset))])
    
    
    chunk_size = CHUNK_SIZE
    start = 0

    num_examples = len(english_dataset)

    for i in range(start, num_examples, chunk_size):
        print(i, i + chunk_size)
        try:
            translated_dataset = load_dataset(TRANSLATED_DATASET_NAME, split="train")
            translated_ids = {item["id"] for item in translated_dataset}
        except:
            translated_ids = set()

        try:
            with open(OUTPUT_FILE, "r") as f:
                lines = f.readlines()
                for line in lines:
                    if not line.strip():
                        continue
                    translated_ids.add(json.loads(line)["id"])
        except:
            pass

        english_dataset_chunk = english_dataset.to_list()[i : i + chunk_size]

        rows_to_translate = [
            row for row in english_dataset_chunk if row["id"] not in translated_ids
        ]

        asyncio.run(concrun(rows_to_translate))
