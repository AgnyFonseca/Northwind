import os
import psycopg2
import csv
from datetime import datetime

# Database connection parameters
DB_HOST = "localhost"
DB_PORT = 5434
DB_NAME = "indicium-northwind"
DB_USER = "northwind_user"
DB_PASSWORD = "thewindisblowing"

# Connect to the database
conn = psycopg2.connect(host=DB_HOST, port=DB_PORT, database=DB_NAME, user=DB_USER, password=DB_PASSWORD)
cur = conn.cursor()

date_str = datetime.now().strftime("%Y-%m-%d")

# List of tables and corresponding CSV files
tables = {
    'categories': 'categories.csv',
    'customers': 'customers.csv',
    'customer_demographics': 'customer_demographics.csv',
    'region': 'region.csv',
    'territories': 'territories.csv',
    'employees': 'employees.csv',
    'employee_territories': 'employee_territories.csv',
    'suppliers': 'suppliers.csv',
    'products': 'products.csv',
    'shippers': 'shippers.csv',
    'orders': 'orders.csv',
    'us_states': 'us_states.csv',
    'order_details': 'order_details.csv',
}

# Iterate over tables and insert data from corresponding CSV files
for table, csv_file in tables.items():
    file_name = f"data/csv/{table}/{date_str}/{csv_file}"
    print(file_name)
    
    # Open CSV file and read rows into a list
    with open(file_name, encoding='utf-8', newline='') as f:
        reader = csv.reader(f)
        rows = [row for row in reader]

    if len(rows) > 1:
        # Replace empty or null values with SQL NULL keyword
        for i in range(len(rows)):
            for j in range(len(rows[i])):
                if not rows[i][j]:
                    rows[i][j] = None
                elif "'" in rows[i][j]:
                    rows[i][j] = rows[i][j].replace("'", "")

        # Insert data into the table
        columns = ', '.join(rows[0])
        placeholders = ', '.join(['%s' for _ in range(len(rows[0]))])
        for row in rows[1:]:
            if table == 'employees':
                # Insert NULL into reports_to column for now because of fk violation constraint
                row = list(row)
                row[16] = None
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"
            cur.execute(query, row)

# Update reports_to values for employees
with open(f"data/csv/employees/{date_str}/employees.csv", encoding='utf-8', newline='') as f:
    reader = csv.reader(f)
    rows = [row for row in reader]
    for row in rows[1:]:
        if row[16]:
            employee_id = row[0]
            reports_to = row[16]
            # Update the reports_to value for the current employee
            cur.execute(f"UPDATE employees SET reports_to = %s WHERE employee_id = %s", (reports_to, employee_id))

# Commit changes and close connection
conn.commit()
cur.close()
conn.close()
