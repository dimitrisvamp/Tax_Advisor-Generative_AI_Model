import sqlite3 as sql


def dbConnector():
    
    # Connect to taxes.db
    cursor, conn = connectDB()

    # Show available tables from taxes.db
    show_tables_query = "SELECT name FROM sqlite_master WHERE type='table';"
    cursor.execute(show_tables_query)
    tables = cursor.fetchall()

    # Create table taxes if it doesnt exist or do nothing if already exists
    if ('tax_data',) in tables:
        print("\nTable for taxes exists!")
        pass
    else:
        print("\nTable for taxes doesn't exist!\n")
        createTable(cursor, conn)

    return cursor, conn



def connectDB():

    # Connect to db
    conn = sql.connect("taxes.db")
    print(conn.total_changes)

    cursor = conn.cursor()

    return cursor, conn

# Create table to store the tax data
def createTable(cursor, conn):
    print("\nCreate table for taxes\n")

    create_table_query = ''' 
    CREATE TABLE tax_data (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    income INTEGER,
    expenses INTEGER,
    advice TEXT
    )
    ''' 

    cursor.execute(create_table_query)
    conn.commit()
    conn.close()

