from bs4 import BeautifulSoup
from mock import Mock
from site_parser.category_parser import CategoryPageParser
from site_parser.post_parser import PostPageParser

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


def mock_BeautifulSoup():
    return Mock(BeautifulSoup)


def mock_link_tag(href):
    link = Mock()
    link.attrs = dict(href=href)
    return link


def mock_category_parser():
    return Mock(CategoryPageParser)


def mock_post_parser():
    return Mock(PostPageParser)