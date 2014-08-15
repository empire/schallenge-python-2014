from site_parser.category_parser import CategoryPageParser
from site_parser.helpers import build_beautiful_soup_from_path

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


def test_get_post_links():
    soup = build_beautiful_soup_from_path('sample/sample_category.html')
    parser = CategoryPageParser(soup)

    links = parser.get_post_links()
    assert list(links) == [
        "http://p30download.com/fa/entry/53201/", "http://p30download.com/fa/entry/53304/",
        "http://p30download.com/fa/entry/50296/", "http://p30download.com/fa/entry/53035/",
        "http://p30download.com/fa/entry/52929/", "http://p30download.com/fa/entry/52780/",
        "http://p30download.com/fa/entry/52677/", "http://p30download.com/fa/entry/52430/",
        "http://p30download.com/fa/entry/51855/"]

def test_get_pagination_pages():
    soup = build_beautiful_soup_from_path('sample/sample_category.html')
    parser = CategoryPageParser(soup)

    links = parser.get_pagination_pages()
    assert list(links) == [
        "http://p30download.com/fa/ebook/category/literary/page/2", "http://p30download.com/fa/ebook/category/literary/page/3",
        "http://p30download.com/fa/ebook/category/literary/page/4", "http://p30download.com/fa/ebook/category/literary/page/5",
        "http://p30download.com/fa/ebook/category/literary/page/17", "http://p30download.com/fa/ebook/category/literary/page/2"
    ]
