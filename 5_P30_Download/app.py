import json
from db.post import add_update_product, find_posts
from site_crawler.crawler import extract_sample_posts_info

for i in xrange(20):
    for post_json in extract_sample_posts_info(20):
        add_update_product(json.loads(post_json))
        # print post_json.decode('unicode-escape')

find_posts("download")
