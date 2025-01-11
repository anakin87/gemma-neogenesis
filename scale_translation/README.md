# 🌐⚙️ Scale Translation Example

The translation process described in the notebook is simple and effective for demonstration purposes. However, scaling this process to handle large datasets requires additional engineering efforts to parallelize tasks, manage rate limits, and minimize data loss.

This folder contains a basic example of how to scale the translation process. While the code is not polished, it can serve as a useful starting point.

- [`translate_instructions.py`](translate_instructions.py): Translates the system and user message of an English dataset to another language (e.g. Italian).
  - retry mechanism with clients using different timeout
  - handling of concurrent requests
  - basic error management
  - saves intermediate results in a JSONL file
- [`monitor_sync_dataset.py`](monitor_sync_dataset.py): Monitors the translation process and periodically pushes the dataset to the hub.
  - reads from the JSONL file
  - skips examples with encoding issues
  - cleans up memory


