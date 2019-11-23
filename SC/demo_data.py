from SQLite import SQLite


def create_table(db, table, schema):
    q = f"CREATE TABLE IF NOT EXISTS {table} {schema}"
    with SQLite(db) as c:
        c.execute(q)
        print("Created Table!")


def insert(db, table, data):
    q = f"INSERT INTO {table} VALUES (?, ?, ?)"
    with SQLite(db) as c:
        c.executemany(q, data)
        print("Inserted Data!")


def count_rows(db, table):
    q = f"SELECT COUNT(*) FROM {table}"
    with SQLite(db) as c:
        count = list(c.execute(q))[0][0]
        print(f"There are {count} rows")


def query(db, q):
    with SQLite(db) as c:
        return list(c.execute(q))


def main():
    db = "demo_data.sqlite3"
    table = "demo"
    schema = "(s VARCHAR(1), x INT, y INT)"
    data = [('g', 3, 9), ('v', 5, 7), ('f', 8, 7)]

    print("Opening Connection and creating table...")
    create_table(db, table, schema)
    print("\n")

    print("Inserting data...")
    insert(db, table, data)
    print("\n")

    count_rows(db, table)
    print("\n")

    gte5 = query(db, f"SELECT COUNT(*) FROM {table} WHERE x >=5 AND y >= "
                     f"5")[0][0]
    print(f"There are {gte5} rows where x and y are at least 5")
    print("\n")

    dist_y = query(db, f"SELECT COUNT(DISTINCT y) FROM {table}")[0][0]
    print(f"There are {dist_y} unique values of y")
    print("\n")


if __name__ == '__main__':
    main()
