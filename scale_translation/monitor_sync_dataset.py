import os
from datasets import load_dataset, Dataset, concatenate_datasets
import json
import time
import gc


# CONFIG
os.environ["HF_TOKEN"] = "..."  # specify your token
TRANSLATED_DATASET_NAME = "anakin87/FineTome-single-turn-dedup-ita"
OUTPUT_FILE = "instructions_ita.json"


def get_existing_dataset():
    """Get existing dataset using streaming."""
    try:
        return load_dataset(TRANSLATED_DATASET_NAME, split="train")
    except Exception as e:
        print(f"Error loading dataset: {e}")
        return None


def process_new_items(file_path, existing_dataset):
    """Process new items from file and push to hub."""
    existing_ids = {item["id"] for item in existing_dataset}
    new_items = []

    with open(file_path, "r") as f:
        for line in f:
            if not line.strip():
                continue

            try:
                row = json.loads(line)
                if row["id"] not in existing_ids:
                    new_items.append(row)
                    existing_ids.add(row["id"])  # Update set to avoid duplicates
            except json.JSONDecodeError as e:
                print(f"Error parsing JSON line: {e}")
                continue

    valid_items = []
    for item in new_items:
        try:
            # Try converting item to a Dataset element to check for encoding issues
            Dataset.from_list([item])
            valid_items.append(item)
        except Exception as e:
            print(f"Error processing item {item.get('id', 'unknown')}: {e}")
            continue

    if valid_items:
        # Create dataset from new items
        new_dataset = Dataset.from_list(new_items)

        # Concatenate with existing dataset
        updated_dataset = concatenate_datasets([existing_dataset, new_dataset])

        # Push the concatenated dataset
        updated_dataset.push_to_hub(TRANSLATED_DATASET_NAME)
        print(f"Pushed {len(new_items)} new items")

        # Clean up
        del new_dataset
        del updated_dataset
        gc.collect()


def main():
    while True:
        print("Checking for new items...")
        try:
            # Get existing dataset
            existing_dataset = get_existing_dataset()
            if existing_dataset is None:
                existing_dataset = Dataset.from_list([])

            # Process new items
            process_new_items(OUTPUT_FILE, existing_dataset)

            # Force garbage collection
            del existing_dataset
            gc.collect()

            print("Completed processing cycle")
        except Exception as e:
            print(f"Error in main loop: {e}")

        time.sleep(300)


if __name__ == "__main__":
    main()
