import sqlite3


def unpack(d):
    return ", ".join(map(str, d.items()))  # map(), just for kicks


def open_connection(db):
    try:
        conn = sqlite3.connect(db)
        return conn
    except sqlite3.Error as e:
        print(e)


def create_table(db, table, schema):
    conn = open_connection(db)
    q = f"CREATE TABLE {table} {schema}"


d = {"s": "a", "b": "d"}
print(unpack(d))
