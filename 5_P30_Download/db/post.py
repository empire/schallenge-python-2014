from db.connection import _get_products_db
from pymongo import MongoClient

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


def _get_products_collection():
    db = _get_products_db()
    return db.products


def add_update_product(product):
    """
    We can use upsert instead of find/insert, but as in question mentioned, we must check for modification,
    if there is any modification in data then product must be updated.
    It's not thread-safe
    """
    collection = _get_products_collection()
    product_in_db = collection.find_one(dict(URL=product['URL']))
    if None == product_in_db:
        collection.insert(product)
        return

    del product_in_db['_id']
    if product != product_in_db:
        collection.update(dict(URL=product['URL']), product)

def find_posts(search):
    """
    The best solution is using text search inside MongoDB, db.runCommand("text", search=search), but this command is
    not enabled by default.
    Another solution is using map/reduce, but increase complexity of this function little more, and I don't know if
    that is really needed!
    I am using simple search instead of wring map, reduce function
    """
    products = _get_products_collection()
    properties = [u'category', u'description', u'views', u'URL', u'name']
    expressions = map(lambda prp: {prp: {"$regex": '.*%s.*'%search}}, properties)
    search_expression = {'$or': expressions}
    print list(products.find(search_expression))
