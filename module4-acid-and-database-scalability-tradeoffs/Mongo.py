from MongoDBConnectionManager import MongoDBConnectionManager


class Mongo:
    """a MongoDB helper class"""

    def __init__(self, user, password, database, collection):
        self.user = user
        self.password = password
        self.database = database
        self.collection = collection

    def query(self, query={}, projection={}):
        with MongoDBConnectionManager(self.user, self.password) as mongo:
            db = getattr(mongo.connection, self.database)
            collection = getattr(db, self.collection)
            data = collection.find(query, projection)
            return data

    def count(self, query={}):
        with MongoDBConnectionManager(self.user, self.password) as mongo:
            db = getattr(mongo.connection, self.database)
            collection = getattr(db, self.collection)
            data = collection.count_documents(query)
            return data

    def distinct(self, field="", query={}):
        with MongoDBConnectionManager(self.user, self.password) as mongo:
            db = getattr(mongo.connection, self.database)
            collection = getattr(db, self.collection)
            data = collection.distinct(field, query)
            return data

    def count_distinct(self, field="", query={}):
        return len(self.distinct(field, query))
