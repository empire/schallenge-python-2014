from http.exceptions.http_exception import BadRequestHttpException, NotImplementedHttpException, \
    MethodNotAllowedHttpException
from http.http_request import HTTPRequest
from http.request_builder import process_http_message, parse_initial_line, parse_headers, set_request_headers, \
    _check_method
from mock import patch, Mock, DEFAULT, MagicMock
import pytest
from tests.http_test import mock_http_request

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


def test_parse_initial_line_invalid_line():
    assert parse_initial_line('blah blah blah blah') == ('blah', 'blah blah', 'blah')
    assert parse_initial_line('blah') == ('blah', None, None)
    assert parse_initial_line('blah blah') == ('blah', 'blah', None)

def test_parse_initial_line_without_path():
    invalid_line = 'GET'
    (method, path, protocol) = parse_initial_line(invalid_line)
    assert method == 'GET'
    assert path == None
    assert protocol == None

def test_parse_initial_line_without_protocol():
    invalid_line = 'GET /sample'
    (method, path, protocol) = parse_initial_line(invalid_line)
    assert method == 'GET'
    assert path == '/sample'
    assert protocol == None

def test_parse_initial_line_with_invalid_protocol():
    invalid_line = 'GET /sample page'
    (method, path, protocol) = parse_initial_line(invalid_line)
    assert method == 'GET'
    assert path == '/sample'
    assert protocol == 'page'

def test_parse_initial_line_valid_line():
    invalid_line = 'GET /assets/images/bg.jpg HTTP/1.1'
    (method, path, protocol) = parse_initial_line(invalid_line)
    assert method == 'GET'
    assert path == '/assets/images/bg.jpg'
    assert protocol == 'HTTP/1.1'


@pytest.fixture(scope="function", params=[
    ['A'],
    ['B B'],
    ['A: 1', 'A 1'],
])
def invalid_headers(request):
    return request.param

def test_parse_headers_invalid_header(invalid_headers):
    with pytest.raises(BadRequestHttpException):
        parse_headers(invalid_headers)

@pytest.fixture(scope="function", params=[
    (['A: 1'],                 {'A':   '1'}),
    (['  B B : 1   '],         {'B B': '1'}),
    (['A: 1', 'B:  A B C D '], {'A':   '1', 'B': 'A B C D'}),
    (
        ['User-Agent: client/1.2.3', 'Host: localhost:8181', 'Accept: */*'],
        {'User-Agent': 'client/1.2.3', 'Host': 'localhost:8181', 'Accept': '*/*'}
    ),
])
def valid_headers(request):
    return request.param

def test_parse_headers_valid_header(valid_headers):
    header_bag = parse_headers(valid_headers[0])
    assert header_bag == valid_headers[1]

@patch('http.request_builder.parse_headers')
def test_set_request_headers_without_host_must_raise_bad_request_exception(parse_headers):
    """

    :type parse_headers: mock.MagicMock
    """
    request = mock_http_request()
    headers = 'User-Agent: client/1.2.3'
    headers_bag = {'User-Agent': 'client/1.1.3'}
    parse_headers.return_value = headers_bag

    with pytest.raises(BadRequestHttpException):
        set_request_headers(request, headers)

    parse_headers.assert_called_once_with(headers)

@patch('http.request_builder.parse_headers')
def test_set_request_headers_with_host(parse_headers):
    """

    :type parse_headers: mock.MagicMock
    """
    request = mock_http_request()
    headers = 'Host: localhost:8181'
    headers_bag = {'Host': 'localhost:8181'}
    parse_headers.return_value = headers_bag

    set_request_headers(request, headers)

    parse_headers.assert_called_once_with(headers)
    assert request.headers == headers_bag

def test_process_http_message():
    with patch.multiple('http.request_builder',
                        parse_initial_line=DEFAULT,
                        build_request=DEFAULT,
                        _check_method=DEFAULT,
                        set_request_headers=DEFAULT) as values:
        # Character \r is removed from line #2, #3
        message = '''POST /index.html HTTP/1.1\r
User-Agent: Ocean/14.08.01
Host: localhost:8181
Accept: text/xml\r
'''
        values['parse_initial_line'].return_value = 'POST', '/index.html', 'HTTP/1.1'
        request = mock_http_request()

        result = process_http_message(request, message)

        values['parse_initial_line'].assert_called_once_with('POST /index.html HTTP/1.1')
        values['build_request'].assert_called_once_with(request, 'POST', '/index.html')
        values['_check_method'].assert_called_once_with('POST')
        values['set_request_headers'].assert_called_once_with(request, [
            'User-Agent: Ocean/14.08.01', 'Host: localhost:8181', 'Accept: text/xml'
        ])
        assert result == None

def test_check_method():
    with pytest.raises(MethodNotAllowedHttpException):
        _check_method('POST')

