import csv
from datetime import datetime

INPUT_FILE = "magento_dates.csv"
OUTPUT_FILE = "converted_dates.csv"
INPUT_COLUMN_INDEX = 0  # which column has the Magento datetime

def convert_us_to_parts(date_str):
    try:
        # Parse US-style Magento export: MM/DD/YYYY HH:MM
        dt = datetime.strptime(date_str.strip(), "%m/%d/%Y %H:%M")
        # Return full datetime, date part, and time part
        return dt.strftime("%Y-%m-%d %H:%M:%S"), dt.strftime("%Y-%m-%d"), dt.strftime("%H:%M:%S")
    except ValueError:
        return "Invalid", "", ""

def process_file(input_file, output_file):
    with open(input_file, newline='', encoding="utf-8") as infile, \
         open(output_file, 'w', newline='', encoding="utf-8") as outfile:
        
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        # Header
        writer.writerow(["Original", "DateTime", "Date", "Time"])

        for row in reader:
            original = row[INPUT_COLUMN_INDEX]
            dt, date_part, time_part = convert_us_to_parts(original)
            writer.writerow([original, dt, date_part, time_part])

    print(f"Converted file saved as: {output_file}")

if __name__ == "__main__":
    process_file(INPUT_FILE, OUTPUT_FILE)
