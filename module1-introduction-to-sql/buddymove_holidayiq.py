import pandas as pd
import sqlite3

df = pd.read_csv('buddymove_holidayiq.csv')

conn = sqlite3.connect('buddymove_holidayiq.sqlite')
c = conn.cursor()


def total_rows(cursor, table_name):
    cursor.execute(f"SELECT COUNT(*) FROM {table_name}")
    count = cursor.fetchall()
    return count[0][0]


def table_names(cursor):
    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    return cursor.fetchall()


print("Current Tables before Pandas to_sql: ")
print(table_names(c))
print("\n")

df.to_sql("main", conn)

print("Tables after: ")
print(table_names(c))
print("\n")

print("Total Rows: ")
print(total_rows(c, "main"))
print("\n")

print(
    "How many users who reviewed at least 100 Nature in the category also "
    "reviewed at least 100 in the Shopping category?")

q = """SELECT COUNT(*)
    FROM main
    WHERE Nature >= 100
    AND Shopping >= 100"""

c.execute(q)
print(c.fetchall()[0][0])

print("\n")

print("What are the average number of reviews for each category?")

q = """SELECT 
    AVG(Sports),
    AVG(Religious),
    AVG(Nature),
    AVG(Theatre),
    AVG(Shopping),
    AVG(Picnic)
    FROM main"""

c.execute(q)
print(c.fetchall())

conn.close()
