from SQLite import SQLite


def main():
    db = "northwind_small.sqlite3"
    with SQLite(db) as c:
        ten_most_expensive_products = "SELECT ProductName, UnitPrice " \
                                      "FROM Product " \
                                      "ORDER BY UnitPrice " \
                                      "DESC " \
                                      "LIMIT 10"

        c.execute(ten_most_expensive_products)
        print(c.fetchall())
        print("\n")

        average_employee_age_at_hire_time = "SELECT AVG(HireDate - " \
                                            "BirthDate) FROM Employee"
        c.execute(average_employee_age_at_hire_time)
        print(c.fetchone()[0])
        print("\n")


if __name__ == '__main__':
    main()
