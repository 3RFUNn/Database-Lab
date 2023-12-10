# Import libraries
import sqlite3

# Define a function that takes a database file name and a list of table names as arguments
def describe_tables(db_file, table_list):
    # Create a connection to the database file
    conn = sqlite3.connect(db_file)
    # Create a cursor object to execute queries
    cur = conn.cursor()
    # Loop through the table names
    for table in table_list:
        # Execute a query to get the column names and types of the table
        cur.execute(f"PRAGMA table_info({table})")
        # Fetch the results as a list of tuples
        columns = cur.fetchall()
        # Print the table name and the columns
        print(f"Description of {table}:")
        for column in columns:
            print(column[1], column[2])
    # Close the connection
    conn.close()

# Example usage
describe_tables("database.sqlite",["Country","League"])
