from Mongo import Mongo
import os
from pprint import pprint as pprint
from dotenv import load_dotenv

load_dotenv()


def main():
    questions = """
        How many total Characters are there?
        How many of each specific subclass?
        How many total Items?
        How many of the Items are weapons? How many are not?
        How many Items does each character have? (Return first 20 rows)
        How many Weapons does each character have? (Return first 20 rows)
        On average, how many Items does each Character have?
        On average, how many Weapons does each character have?
    """
    questions = questions.split("\n")[1:-1]
    user = os.getenv("DB_USER")
    password = os.getenv("DB_PASSWORD")
    db = "rpg"
    collection = "rpg_collection"

    rpg = Mongo(user, password, db, collection)

    print(questions[0].strip())
    print(rpg.count())
    print("\n")

    print(questions[1].strip())
    subclasses = ['fighter', 'mage', 'cleric', 'thief']
    for subclass in subclasses:
        count = rpg.count({subclass: {"$exists": True}})
        print(f"{subclass}: {count}")
    print("\n")

    print(questions[2].strip())
    print(rpg.count_distinct("inventory"))
    print("\n")

    print(questions[3].strip())
    print(list(rpg.query({"inventory.power": {"$exists": True}},
                         {"inventory.name": 1, "inventory.power": 1})))


if __name__ == '__main__':
    main()
