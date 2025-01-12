# 📚 References

Curated collection of key resources and references used in the notebook.

## 💎💬🇮🇹 Gemma Neogenesis
- [Kaggle notebook](ADD_LINK)
- [Hugging Face collection](ADD_LINK): contains all datasets, models, and HF Space to try the model.

## 🔧 Libraries
- [HF TRL](https://huggingface.co/docs/trl/index): the great library used for SFT and DPO.
- [Spectrum](https://github.com/cognitivecomputations/spectrum): library that implements the Spectrum method for targeted training on Signal to Noise Ratio.
- [lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness): framework for few-shot evaluation of language models. 
- [vLLM](https://github.com/vllm-project/vllm): high-throughput and memory-efficient inference and serving engine for LLMs.
- [Haystack](https://haystack.deepset.ai/): AI orchestration framework to build customizable, production-ready LLM applications.
- [Distilabel](https://github.com/argilla-io/distilabel): a framework by Argilla for synthetic data generation and AI feedback.



## 🏋️‍♂️ Training of Language Models
- [smol-course](https://github.com/huggingface/smol-course): a practical course by Hugging Face on aligning Language Models for your use case.
- [RLHF and alternatives](https://argilla.io/blog/mantisnlp-rlhf-part-1): a series of blog posts by Argilla and MantisNLP.

### Preference Tuning
#### Reinforcement Learning from Human Feedback
- [InstructGPT: Aligning language models to follow instructions](https://openai.com/index/instruction-following/): the work that popularized RLHF.
- [RLHF: Reinforcement Learning from Human Feedback](https://huyenchip.com/2023/05/02/rlhf.html) by Chip Huyen.

#### Direct Preference Optimization
- [Direct Preference Optimization: Your Language Model is Secretly a Reward Model](https://arxiv.org/abs/2305.18290).
- [Is DPO Superior to PPO for LLM Alignment? A Comprehensive Study](https://arxiv.org/abs/2404.10719).
- [Disentangling Length from Quality in Direct Preference Optimization](https://arxiv.org/abs/2403.19159v2).

### Technical reports with interesting post-training insights
- [The Llama 3 Herd of Models](https://arxiv.org/abs/2407.21783): Llama 3 technical report.
- [Tulu 3: Pushing Frontiers in Open Language Model Post-Training](https://arxiv.org/abs/2411.15124): Tulu 3 technical report.
  
## ⚡ Efficient Fine-tuning
- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14201).
- [LoRA vs Full Fine-tuning: An Illusion of Equivalence](https://arxiv.org/abs/2410.21228).
- [Spectrum: Targeted Training on Signal to Noise Ratio](https://arxiv.org/abs/2406.06623).
- [Methods and tools for efficient training on a single GPU](https://huggingface.co/docs/transformers/perf_train_gpu_one): insightful page on Hugging Face docs.

## 🧪 Synthetic Data Generation
- [Magpie: Alignment Data Synthesis from Scratch by Prompting Aligned LLMs with Nothing](https://arxiv.org/abs/2406.08464).
- [Generating multilingual instruction datasets with Magpie](https://huggingface.co/blog/anakin87/multilingual-magpie).

## 🏅 Evaluation/benchmarks
### Leaderboards
- [Open ITA LLM Leaderboard](https://huggingface.co/spaces/mii-llm/open_ita_llm_leaderboard): most popular benchmark for evaluating LLMs in Italian.
- [Collection of HF Leaderboards](https://huggingface.co/collections/clefourrier/leaderboards-and-benchmarks-64f99d2e11e92ca5568a7cce)

### Classic benchmarks
- [Measuring Massive Multitask Language Understanding](https://arxiv.org/abs/2009.03300).
- [Think you have Solved Question Answering? Try ARC, the AI2 Reasoning Challenge](https://arxiv.org/abs/1803.05457v1).
- [HellaSwag: Can a Machine Really Finish Your Sentence?](https://arxiv.org/abs/1905.07830).

### Instruction following/chat benchmarks
- [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685).
- [AlpacaEval](https://github.com/tatsu-lab/alpaca_eval): An Automatic Evaluator for Instruction-following Language Models.
- [Instruction-Following Evaluation for Large Language Models](https://arxiv.org/abs/2311.07911).

# Other
- [Evaluating the Effectiveness of LLM-Evaluators (aka LLM-as-Judge)](https://eugeneyan.com/writing/llm-evaluators/): good long read by Eugene Yan.
- [How to generate text: using different decoding methods for language generation with Transformers](https://huggingface.co/blog/how-to-generate): a good read by Patrick von Platen on decoding/sampling strategies.
- [Small Language Models on a smartphone](https://www.linkedin.com/posts/stefano-fiorucci_llm-genai-edgecomputing-activity-7183365537618411520-PU2s/): LinkedIn post.
