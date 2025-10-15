# Magento Date & Time Converter

A simple Python script to convert Magento-exported date-time values (formatted as `MM/DD/YYYY HH:MM`) into ISO-standard UK-friendly formats (`YYYY-MM-DD HH:MM:SS`). It also extracts the date and time parts separately for easy use in Excel or other systems.

---

## ✅ Features

- Converts US-style datetime strings (`MM/DD/YYYY HH:MM`) into:
  - Full ISO datetime (`YYYY-MM-DD HH:MM:SS`)
  - Date-only (`YYYY-MM-DD`)
  - Time-only (`HH:MM:SS`)
- Outputs a clean CSV with original and parsed columns.
- Simple and fast for local use.

---

## 📂 Input Format

**File:** `magento_dates.csv`

One Magento-style datetime string per line:
```

10/14/2025 23:10
10/14/2025 23:16
10/14/2025 23:28

````

---

## 📤 Output Format

**File:** `converted_dates.csv`

| Original           | DateTime              | Date        | Time     |
|--------------------|------------------------|-------------|----------|
| 10/14/2025 23:10   | 2025-10-14 23:10:00    | 2025-10-14  | 23:10:00 |
| 10/14/2025 23:16   | 2025-10-14 23:16:00    | 2025-10-14  | 23:16:00 |

---

## 🚀 Usage

1. Install Python 3 if not already installed.
2. Place your input file `magento_dates.csv` in the same directory.
3. Run the script:

```bash
python date_and_time_convert_magento_dates.py
````

4. The output will be saved as `converted_dates.csv` in the same folder.

---

## ⚠️ Notes

* This script assumes all dates are in `MM/DD/YYYY HH:MM` format (US-style Magento exports).
* Invalid or unparseable values will be flagged as `"Invalid"` in the output.
* If your input format is different (e.g. `DD/MM/YYYY`), the parser logic must be adjusted.

---

## 🛠 Customisation

* To change the input or output file names, edit the variables at the top of the script:

  ```python
  INPUT_FILE = "your_input_file.csv"
  OUTPUT_FILE = "your_output_file.csv"
  ```

---

## 📃 License

MIT — free to use, modify, and share.

---
