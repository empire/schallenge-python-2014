from http.http_request import HTTPRequest
from mock import Mock, MagicMock
from pip._vendor.requests.packages.urllib3.response import HTTPResponse

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


def mock_http_response():
    response = Mock(HTTPResponse)
    response.status = None
    response.content = ''
    response.content_type = None
    return response


def mock_http_request():
    request = Mock(HTTPRequest)
    return request
