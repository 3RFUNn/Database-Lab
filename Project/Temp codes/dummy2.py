# Import sqlite3 library
import sqlite3

# Connect to the population_data.db file
conn = sqlite3.connect("population_data.db")

# Create a cursor object
cur = conn.cursor()

# Execute a query to get the names of the tables
cur.execute("""SELECT name FROM sqlite_master WHERE type='table';""")

# Fetch the results as a list of tuples
tables = cur.fetchall()

# Loop through each table
for table in tables:
    # Get the table name
    table_name = table[0]
    # Execute a query to get the column names of the table
    cur.execute(f"""PRAGMA table_info({table_name});""")
    # Fetch the results as a list of tuples
    columns = cur.fetchall()
    # Print the table name and the column names
    print(f"The columns in {table_name} are:")
    for column in columns:
        print(column[1])
