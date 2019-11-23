from pymongo import MongoClient


class MongoDBConnectionManager:
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.connection = None

    def __enter__(self):
        self.connection = MongoClient(
            f"mongodb+srv://{self.username}:"
            f"{self.password}@cluster0-0jkyy.mongodb.net/test"
            "?retryWrites=true&w=majority")
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        self.connection.close()
