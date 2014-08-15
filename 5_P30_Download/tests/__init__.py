from bs4 import BeautifulSoup
from mock import Mock

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


def mock_BeautifulSoup():
    return Mock(BeautifulSoup)


def mock_link_tag(href):
    link = Mock()
    link.attrs = dict(href=href)
    return link
