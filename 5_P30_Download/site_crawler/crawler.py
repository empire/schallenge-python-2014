import urllib2
import StringIO
from site_parser.category_parser import CategoryPageParser
from site_parser.index_parser import get_categories, pick_random_category
from site_parser.helpers import build_beautiful_soup, build_beautiful_soup_from_path
from site_parser.post_parser import PostPageParser

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def get_url_content(url):
    response = urllib2.urlopen(url)
    return response.read()


def get_soup_from_url(url):
    # print 'Extract url: ', url
    html_doc = get_url_content(url)
    return build_beautiful_soup(html_doc)


def category_parser_from_url(category_url):
    category_soup = get_soup_from_url(category_url)
    return CategoryPageParser(category_soup)

def extract_post_links(category_url, post_links):
    parser = category_parser_from_url(category_url)
    post_links += list(parser.get_post_links())

    return parser

def extract_sample_category_from_site():
    soup = get_soup_from_url('http://p30download.com/')
    # soup = build_beautiful_soup_from_path('sample/sample_post.html')
    return pick_random_category(soup)


def extract_posts_link(links_count):
    post_links = []
    parser = extract_post_links(extract_sample_category_from_site(), post_links)
    for category_page in parser.get_pagination_pages():
        if len(post_links) >= links_count:
            break
        extract_post_links(category_page, post_links)
    return post_links[:links_count]


def extract_sample_posts_info(posts_count):
    for post_url in extract_posts_link(posts_count):
        parser = PostPageParser.parser_factory(get_soup_from_url(post_url))
        yield parser.jsonify()

