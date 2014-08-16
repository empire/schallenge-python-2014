from pymongo.mongo_client import MongoClient

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def _get_mongo_client():
    return MongoClient('localhost', 27017)


def _get_products_db():
    client = _get_mongo_client()
    return client.p30download
