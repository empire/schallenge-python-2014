from site_parser.first_page import get_categories, pick_random_category
from site_parser.helpers import build_beautiful_soup

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

with open('sample/sample_post.html') as sample_pag:
    sample_content = ''.join(sample_pag.readlines())
    soup = build_beautiful_soup(sample_content)
    print pick_random_category(soup)
