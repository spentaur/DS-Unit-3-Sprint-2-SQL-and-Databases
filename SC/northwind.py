from SQLite import SQLite
from pprint import pprint


def main():
    db = "northwind_small.sqlite3"
    with SQLite(db) as c:
        ten_most_expensive_products = "SELECT ProductName, UnitPrice " \
                                      "FROM Product " \
                                      "ORDER BY UnitPrice " \
                                      "DESC " \
                                      "LIMIT 10"

        c.execute(ten_most_expensive_products)
        pprint(c.fetchall())
        print("\n")

        average_employee_age_at_hire_time = "SELECT AVG(HireDate - " \
                                            "BirthDate) FROM Employee"
        c.execute(average_employee_age_at_hire_time)
        print(c.fetchone()[0])
        print("\n")

        ten_most_expensive_products_with_suppliers = "SELECT p.ProductName, " \
                                                     "p.UnitPrice, " \
                                                     "s.CompanyName " \
                                                     "FROM Product p " \
                                                     "JOIN Supplier s " \
                                                     "ON " \
                                                     "p.SupplierId = s.Id " \
                                                     "ORDER BY p.UnitPrice " \
                                                     "DESC LIMIT 10"

        c.execute(ten_most_expensive_products_with_suppliers)
        pprint(c.fetchall())
        print("\n")

        largest_category = "SELECT p.CategoryId, " \
                           "c.CategoryName, " \
                           "COUNT(*) as count " \
                           "FROM Product p " \
                           "JOIN Category c " \
                           "ON c.Id = p.CategoryId " \
                           "GROUP BY p.CategoryId " \
                           "ORDER BY count " \
                           "DESC " \
                           "LIMIT 10"
        c.execute(largest_category)
        pprint(c.fetchall())


if __name__ == '__main__':
    main()
