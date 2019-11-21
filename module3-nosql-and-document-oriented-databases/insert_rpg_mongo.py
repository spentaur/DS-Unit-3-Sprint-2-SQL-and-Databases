import pymongo
import os
from dotenv import load_dotenv

load_dotenv()


def connect_to_mongo():
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")

    client = pymongo.MongoClient(
        f"mongodb+srv://{db_user}:"
        f"{db_password}@cluster0-0jkyy.mongodb.net/rpg"
        "?retryWrites=true&w=majority")
    db = client.rpg

    return db


def main():
    connect_to_mongo()


if __name__ == '__main__':
    main()
