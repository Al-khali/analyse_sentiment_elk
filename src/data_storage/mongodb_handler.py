from pymongo import MongoClient

class MongoDBHandler:
    def __init__(self, uri="mongodb://localhost:27017/"):
        self.client = MongoClient(uri)
        self.db = self.client['social_media_data']
        self.collection = self.db['posts']

    def insert_post(self, post_data):
        return self.collection.insert_one(post_data)

    def get_posts(self, query={}):
        return list(self.collection.find(query))

    def update_post(self, post_id, update_data):
        return self.collection.update_one({'id': post_id}, {'$set': update_data})

    def delete_post(self, post_id):
        return self.collection.delete_one({'id': post_id})

    def close_connection(self):
        self.client.close()