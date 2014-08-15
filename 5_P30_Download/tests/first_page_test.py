from bs4 import BeautifulSoup
from mock import Mock, patch, DEFAULT
from site_parser.first_page import get_categories, extract_categories, pick_random_category

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def test_pick_random_category():
    with patch.multiple('site_parser.categories',
                        get_categories=DEFAULT,
                        random=DEFAULT) as values:
        random_mock = values['random']
        get_categories_mock = values['get_categories']
        soup = Mock(BeautifulSoup)

        random_mock.choice.return_value = 'c'
        get_categories_mock.return_value = categories = ['a', 'b', 'c', 'd']

        result = pick_random_category(soup)

        get_categories_mock.assert_called_once_with(soup)
        random_mock.choice.assert_called_once_with(categories)

        assert result == 'c'

def test_get_categories():
    soup = Mock(BeautifulSoup)
    with patch.multiple('site_parser.categories',
                        get_base_categories_lists=DEFAULT,
                        extract_categories=DEFAULT) as values:
        get_base_categories_lists_mock = values['get_base_categories_lists']
        extract_categories_mock = values['extract_categories']
        get_base_categories_lists_mock.return_value = cats = map(mock_link_tag, ['a', 'b'])
        extract_categories_mock.return_value = ['a', 'b']

        result = get_categories(soup)

        get_base_categories_lists_mock.assert_called_once_with(soup)
        extract_categories_mock.assert_called_once_with(cats)

        assert result == ['a', 'b']


def test_extract_categories():
    links = map(mock_link_tag, [
        'http://google.com',
        'http://p30download.com/fa/mobile/category/game/action/',
        'http://p30download.com/fa/tutorial/category/multimedia/',
    ])

    result = extract_categories(links)

    assert result == [
        'http://p30download.com/fa/mobile/category/game/action/',
        'http://p30download.com/fa/tutorial/category/multimedia/'
    ]


def mock_link_tag(href):
    link = Mock()
    link.attrs = dict(href=href)
    return link
