import csv
import os
from datetime import datetime

# Input CSV file path
CSV_FILE_PATH = "../data/order_details.csv"

# Output file directory
output_folder = "data"
date_str = datetime.now().strftime("%Y-%m-%d")
csv_folder = f"{output_folder}/csv/order_details/{date_str}"

os.makedirs(csv_folder, exist_ok=True)

# Read order details from CSV file
with open(CSV_FILE_PATH, mode="r") as csv_file:
    reader = csv.reader(csv_file)
    rows = [row for row in reader]

# Create a CSV file for the order details
file_name = "order_details.csv"
file_path = os.path.join(csv_folder, file_name)

# Write rows to CSV file
with open(file_path, mode='w', encoding='utf-8', newline='') as csv_file:
    writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerows(rows)

