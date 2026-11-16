# Duplicate Data Finder (PS No. 9)

A Python 3 console-based utility that reads entries from a text file, detects duplicate records, counts occurrences, and exports unique entries to `unique.txt`.

## Features
- **Safe File Handling:** Uses `try-except` blocks to gracefully handle missing files and empty file checks.
- **Set & Loop Logic:** Uses Python `set` to identify unique items and loops to count exact repeat frequencies.
- **Flexible Matching Modes:**
  - **Option 1 (Exact Match):** Performs case-sensitive duplicate detection.
  - **Option 2 (Ignore Case & Extra Spaces):** Normalizes letter casing and trims whitespace before comparing.
- **Unique Export:** Automatically writes deduplicated entries to `unique.txt`.

## How to Run
1. Ensure Python 3 is installed on your system.
2. Place your input file (`data.txt`) in the same directory as the script.
3. Run the program from the terminal:
   ```bash
   python duplicate_finder.py
   
