from site_parser.index_parser import get_categories, pick_random_category
from site_parser.helpers import build_beautiful_soup, build_beautiful_soup_from_path

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

soup = build_beautiful_soup_from_path('sample/sample_post.html')
print pick_random_category(soup)
