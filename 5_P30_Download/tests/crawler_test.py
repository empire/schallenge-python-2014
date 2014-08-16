from mock import patch, Mock, DEFAULT
from site_crawler.crawler import get_url_content, get_soup_from_url, category_parser_from_url, extract_post_links, \
    extract_sample_category_from_site, extract_posts_link, extract_sample_posts_info
from site_parser.category_parser import CategoryPageParser
from tests import mock_BeautifulSoup, mock_category_parser, mock_post_parser

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


@patch('site_crawler.crawler.urllib2')
def test_get_url_content(urllib2_mock):
    urllib2_mock.urlopen.return_value = response = Mock()
    response.read.return_value = 'content'

    page_content = get_url_content('url')

    urllib2_mock.urlopen.assert_called_once_with('url')
    response.read.assert_called_once_with()
    assert page_content == 'content'

def test_get_soup_from_url():
    with patch.multiple('site_crawler.crawler', get_url_content=DEFAULT, build_beautiful_soup=DEFAULT) as values:
        get_url_content_mock = values['get_url_content']
        build_beautiful_soup_mock = values['build_beautiful_soup']

        get_url_content_mock.return_value = 'sample html'
        build_beautiful_soup_mock.return_value = soup = mock_BeautifulSoup()

        result = get_soup_from_url('sample url')

        get_url_content_mock.assert_called_once_with('sample url')
        build_beautiful_soup_mock.assert_called_once_with('sample html')
        assert result == soup

def test_category_parser_from_url():
    with patch.multiple('site_crawler.crawler', get_soup_from_url=DEFAULT, CategoryPageParser=DEFAULT) as values:
        get_soup_from_url_mock = values['get_soup_from_url']
        CategoryPageParser_mock = values['CategoryPageParser']
        
        get_soup_from_url_mock .return_value = soup = mock_BeautifulSoup()
        CategoryPageParser_mock.return_value = parser = Mock(CategoryPageParser)

        result = category_parser_from_url('category url')

        get_soup_from_url_mock.assert_called_once_with('category url')
        CategoryPageParser_mock.assert_called_once_with(soup)
        assert result == parser

def test_extract_post_links():
    posts_link = [2, 3]

    with patch.multiple('site_crawler.crawler', category_parser_from_url=DEFAULT, CategoryPageParser=DEFAULT) as values:
        category_parser_from_url_mock = values['category_parser_from_url']
        category_parser_from_url_mock.return_value = parser = mock_category_parser()
        parser.get_post_links.return_value = [5, 7]

        extract_post_links('category url', posts_link)

        category_parser_from_url_mock.assert_called_once_with('category url')
        parser.get_post_links.assert_called_once_with()

    assert posts_link == [2, 3, 5, 7]

def test_extract_sample_category_from_site():
    with patch.multiple('site_crawler.crawler',
                        get_soup_from_url=DEFAULT,
                        pick_random_category=DEFAULT) as values:
        get_soup_from_url_mock = values['get_soup_from_url']
        pick_random_category_mock = values['pick_random_category']
        get_soup_from_url_mock.return_value = soup = mock_BeautifulSoup()
        pick_random_category_mock.return_value = sample = 'http://.../cat/1'

        result = extract_sample_category_from_site()

        get_soup_from_url_mock.assert_called_once_with('http://p30download.com/')
        pick_random_category_mock.assert_called_once_with(soup)

    assert result == sample

def test_extract_posts_link():
    with patch.multiple('site_crawler.crawler',
                        extract_post_links=DEFAULT,
                        extract_sample_category_from_site=DEFAULT) as values:
        extract_post_links_mock = values['extract_post_links']
        extract_sample_category_from_site_mock = values['extract_sample_category_from_site']

        extract_sample_category_from_site_mock.return_value = 'cat1'

        parser = mock_category_parser()
        def extract_post_return_values(url, post_links):
            if url == 'cat1':
                assert post_links == []
                post_links += ['post2', 'post3', 'post5']
                return parser
            elif url == 'page1':
                assert post_links == ['post2', 'post3', 'post5']
                post_links += ['post7', 'post11', 'post13']

        extract_post_links_mock.side_effect = extract_post_return_values

        parser.get_pagination_pages.return_value = ['page1', 'page2', 'page3']

        result = extract_posts_link(5)
        assert 2 == extract_post_links_mock.call_count

    assert result == ['post2', 'post3', 'post5', 'post7', 'post11']


def test_extract_sample_posts_info():
    with patch.multiple('site_crawler.crawler',
                        extract_posts_link=DEFAULT,
                        PostPageParser=DEFAULT,
                        get_soup_from_url=DEFAULT,
                        extract_sample_category_from_site=DEFAULT) as values:
        extract_posts_link_mock = values['extract_posts_link']
        get_soup_from_url_mock = values['get_soup_from_url']
        PostPageParser_mock = values['PostPageParser']

        soup1, soup2 = mock_BeautifulSoup(), mock_BeautifulSoup()
        parser1, parser2 = mock_post_parser(), mock_post_parser()

        extract_posts_link_mock.return_value = ['post1', 'post2']
        get_soup_from_url_mock.side_effect = lambda x: dict(post1=soup1, post2=soup2)[x]
        print soup1, soup2
        PostPageParser_mock.parser_factory.side_effect = lambda x: parser1 if soup1 == x else parser2
        parser1.jsonify.return_value = 'json1'
        parser2.jsonify.return_value = 'json2'

        result = extract_sample_posts_info(3)

        extract_posts_link_mock.assert_called_once_with(3)
        get_soup_from_url_mock.assert_any_call('post1')
        get_soup_from_url_mock.assert_any_call('post2')

        PostPageParser_mock.parser_factory.assert_any_call(soup1)
        PostPageParser_mock.parser_factory.assert_any_call(soup2)

        assert get_soup_from_url_mock.call_count == 2
        assert PostPageParser_mock.parser_factory.call_count == 2
        assert result == 'json1\njson2\n'
