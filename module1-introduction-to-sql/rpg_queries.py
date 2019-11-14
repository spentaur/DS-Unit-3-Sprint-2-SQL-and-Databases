import sqlite3


class RPG:
    """class to access RPG SQLite DataBase"""

    def __init__(self, db):
        self.__conn = sqlite3.connect(db)
        self.__c = self.__conn.cursor()

    def __fetchone(self, q):
        return self.__c.execute(q).fetchone()

    def __fetchall(self, q):
        return self.__c.execute(q).fetchall()

    def __count(self, table_name):
        q = f"SELECT COUNT(*) FROM {table_name}"
        return self.__fetchone(q)[0]

    def get_table_names(self):
        q = "SELECT name FROM sqlite_master WHERE type='table';"
        return sorted(self.__fetchall(q)[0])

    def get_total_characters(self, characters_table):
        return self.__count(characters_table)

    def get_total_subclasses(self, subclass_tables):
        subclass_dict = {}
        for table in subclass_tables:
            subclass = table.split('_')[1].capitalize()
            subclass_dict[subclass] = self.__count(table)
        return subclass_dict

    def get_total_items(self, items_table):
        return self.__count(items_table)

    def get_total_weapons(self, weapons_table):
        return self.__count(weapons_table)

    def get_total_non_weapons(self, weapons_table, items_table):
        items_count = self.get_total_items(items_table)
        weapons_count = self.get_total_weapons(weapons_table)
        return items_count - weapons_count

    def get_total_character_items(self, inventory_table, limit=20):
        q = f"""SELECT character_id, COUNT(*)
            FROM {inventory_table} I
            GROUP BY character_id
            LIMIT {limit}"""
        return self.__fetchall(q)

    def get_total_character_weapons(self, characters_table, weapons_table,
                                    inventory_table, limit):
        q = f"""SELECT C.character_id, ifnull(count, 0)
            FROM {characters_table} C
            LEFT JOIN(
                SELECT I.character_id, COUNT(*) count
                FROM {inventory_table} I
                INNER JOIN {weapons_table} W
                ON W.item_ptr_id = I.item_id
                GROUP BY character_id) X
            ON C.character_id = X.character_id
            LIMIT {limit}"""
        return self.__fetchall(q)

    def get_avg_items(self, inventory_table):
        q = f"""SELECT AVG(count)
            FROM (
                SELECT COUNT(*) count
                FROM {inventory_table} I
                GROUP BY character_id)"""
        return self.__fetchall(q)[0][0]

    def get_avg_weapons(self, characters_table, weapons_table,
                        inventory_table):
        q = f"""SELECT AVG(ifnull(count, 0))
                FROM {characters_table} C
                LEFT JOIN(
                    SELECT I.character_id, COUNT(*) count
                    FROM {inventory_table} I
                    INNER JOIN {weapons_table} W
                    ON W.item_ptr_id = I.item_id
                    GROUP BY character_id) X
                ON C.character_id = X.character_id"""
        return self.__fetchall(q)[0][0]


if __name__ == '__main__':
    db = 'rpg_db.sqlite3'
    characters_table = 'charactercreator_character'
    weapons_table = 'armory_weapon'
    items_table = 'armory_item'
    inventory_table = 'charactercreator_character_inventory'
    subclass_tables = ['charactercreator_cleric', 'charactercreator_fighter',
                       'charactercreator_mage', 'charactercreator_thief']

    rpg = RPG(db)

    print("How many total Characters are there?")
    print(rpg.get_total_characters(characters_table))
    # 302
    print("\n")

    print("How many of each specific subclass?")
    print(rpg.get_total_subclasses(subclass_tables))
    # {'Cleric': 75, 'Fighter': 68, 'Mage': 108, 'Thief': 51}
    print("\n")

    print("How many total Items?")
    print(rpg.get_total_items(items_table))
    # 174
    print("\n")

    print("How many of the Items are weapons? How many are not?")
    print("Weapons: ", rpg.get_total_weapons(weapons_table))
    # 37
    print("Non-Weapons: ",
          rpg.get_total_non_weapons(weapons_table, items_table))
    # 137
    print("\n")

    print("How many Items does each character have? (Return first 20 rows)")
    print(rpg.get_total_character_items(inventory_table, limit=20))
    # [(1, 3), (2, 3), (3, 2), (4, 4), (5, 4), (6, 1), (7, 5), (8, 3), (9,
    # 4), (10, 4), (11, 3), (12, 3), (13, 4), (14, 4), (15, 4), (16, 1),
    # (17, 5), (18, 5), (19, 3), (20, 1)]
    print("\n")

    print("How many Weapons does each character have? (Return first 20 rows)")
    print(rpg.get_total_character_weapons(characters_table, weapons_table,
                                          inventory_table, limit=20))
    # [(1, 0), (2, 0), (3, 0), (4, 0), (5, 2), (6, 0), (7, 1), (8, 0), (9,
    # 0), (10, 0), (11, 1), (12, 0), (13, 0), (14, 0), (15, 0), (16, 0),
    # (17, 0), (18, 0), (19, 0), (20, 1)]
    print("\n")

    print("On average, how many Items does each Character have?")
    print(rpg.get_avg_items(inventory_table))
    # 2.9735099337748343
    print("\n")

    print("On average, how many Weapons does each character have?")
    print(
        rpg.get_avg_weapons(characters_table, weapons_table, inventory_table))
    # 0.6721854304635762
