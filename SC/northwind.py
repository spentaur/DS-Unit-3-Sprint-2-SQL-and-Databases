#!/usr/bin/env python
"""Querying Northwind data with SQLite and Python.

Example output:
[(38, 'Côte de Blaye', 18, 1, '12 - 75 cl bottles', 263.5, 17, 0, 15, 0), (29, 'Thüringer Rostbratwurst', 12, 6, '50 bags x 30 sausgs.', 123.79, 0, 0, 0, 1), (9, 'Mishi Kobe Niku', 4, 6, '18 - 500 g pkgs.', 97, 29, 0, 0, 1), (20, "Sir Rodney's Marmalade", 8, 3, '30 gift boxes', 81, 40, 0, 0, 0), (18, 'Carnarvon Tigers', 7, 8, '16 kg pkg.', 62.5, 42, 0, 0, 0), (59, 'Raclette Courdavault', 28, 4, '5 kg pkg.', 55, 79, 0, 0, 0), (51, 'Manjimup Dried Apples', 24, 7, '50 - 300 g pkgs.', 53, 20, 0, 10, 0), (62, 'Tarte au sucre', 29, 3, '48 pies', 49.3, 17, 0, 0, 0), (43, 'Ipoh Coffee', 20, 1, '16 - 500 g tins', 46, 17, 10, 25, 0), (28, 'Rössle Sauerkraut', 12, 7, '25 - 825 g cans', 45.6, 26, 0, 0, 1)]
[(37.22222222222222,)]
[('Kirkland', 29.0), ('London', 32.5), ('Redmond', 56.0), ('Seattle', 40.0), ('Tacoma', 40.0)]
[('Côte de Blaye', 263.5, 'Aux joyeux ecclésiastiques'), ('Thüringer Rostbratwurst', 123.79, 'Plutzer Lebensmittelgroßmärkte AG'), ('Mishi Kobe Niku', 97, 'Tokyo Traders'), ("Sir Rodney's Marmalade", 81, 'Specialty Biscuits, Ltd.'), ('Carnarvon Tigers', 62.5, 'Pavlova, Ltd.'), ('Raclette Courdavault', 55, 'Gai pâturage'), ('Manjimup Dried Apples', 53, "G'day, Mate"), ('Tarte au sucre', 49.3, "Forêts d'érables"), ('Ipoh Coffee', 46, 'Leka Trading'), ('Rössle Sauerkraut', 45.6, 'Plutzer Lebensmittelgroßmärkte AG')]
[('Confections', 13)]
[(7, 'Robert', 'King', 10)]
"""

import sqlite3

CONN = sqlite3.connect('northwind_small.sqlite3')


def run_queries():
    """Run and print output from queries for sprint challenge questions."""
    # Part 2 queries (no joins)
    expensive_items = 'SELECT * FROM Product ORDER BY UnitPrice DESC LIMIT 10;'
    avg_hire_age = 'SELECT AVG(HireDate - BirthDate) FROM Employee;'
    age_by_city = ('SELECT City, AVG(HireDate - BirthDate) FROM Employee '
                   'GROUP BY City;')
    # Part 3 queries (joins)
    item_suppliers = ('SELECT p.ProductName, p.UnitPrice, s.CompanyName '
                      'FROM Product p, Supplier s WHERE p.SupplierId = s.Id '
                      'ORDER BY p.UnitPrice DESC LIMIT 10;')
    largest_category = ('SELECT c.CategoryName, COUNT(DISTINCT p.Id) '
                        'FROM Category c, Product p WHERE c.Id = p.CategoryId '
                        'GROUP BY 1 ORDER BY 2 DESC LIMIT 1;')
    employee = ('SELECT e.Id, e.FirstName, e.LastName, COUNT(DISTINCT t.Id) '
                'FROM Territory t, Employee e, EmployeeTerritory et '
                'WHERE e.Id = et.EmployeeId AND t.id = et.TerritoryId '
                'GROUP BY 1, 2, 3 ORDER BY 4 DESC LIMIT 1;')
    # Put them all together, run them, print the results
    queries = (expensive_items, avg_hire_age, age_by_city, item_suppliers,
               largest_category, employee)
    curs = CONN.cursor()
    for query in queries:
        print(curs.execute(query).fetchall())

if __name__ == "__main__":
    run_queries()
