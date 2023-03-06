import psycopg2
import os
import csv
from datetime import datetime

# Database connection parameters
DB_HOST = "localhost"
DB_PORT = 5433
DB_NAME = "northwind"
DB_USER = "northwind_user"
DB_PASSWORD = "thewindisblowing"


output_folder = "data"

# Connect to the database
conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
cursor = conn.cursor()

# List of tables to extract data from
tables = ['categories', 'customer_demographics', 'customers', 'employee_territories', 'employees', 'orders', 'products', 'region', 'shippers', 'suppliers', 'territories', 'us_states']

date_str = datetime.now().strftime("%Y-%m-%d")

# Loop through tables and extract data to CSV
for table in tables:
    table_folder = f"{output_folder}/csv/{table}/{date_str}"
    os.makedirs(table_folder, exist_ok=True)

    cursor.execute(f"SELECT * FROM {table}")
    rows = cursor.fetchall()

    # Write data to CSV file
    file_name = f"{table_folder}/{table}.csv"
    with open(file_name, mode='w', encoding='utf-8', newline='') as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
       
        writer.writerow([desc[0] for desc in cursor.description])
        
        for row in rows:
            writer.writerow(row)

# Close database connection
cursor.close()
conn.close()
