import sqlite3
from sqlite3 import Error

# TODO: Function to initialize the database tables.


def create_table(conn, statement):
    """Create a table from the statement.
    :param conn: Connection object
    :param statement: a CREATE TABLE statement
    """
    try:
        c = conn.cursor()
        c.execute(statement)
    except Error as e:
        print(e)


# Try to connect
try:
    conn = sqlite3.connect("recipes.db")
    c = conn.cursor()
except Error as e:
    print(e)


if conn is not None:
    # TODO: Create a recipe table.
    pass
else:
    print("Error! No database connection.")
