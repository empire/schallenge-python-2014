from http.exceptions.http_exception import BadRequestHttpException
from http.handle_requests import handle_user_request, handle_http_request, handle_http_response
from http.http_request import HTTPRequest
from http.http_response import HTTPResponse
from http.routing.route import Route
from mock import Mock, patch, MagicMock, DEFAULT


__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


@patch('http.handle_requests.router')
def test_handle_http_request(router):
    request = Mock(HTTPRequest)
    request.path   = '/welcome'
    request.method = 'GET'
    router.find_route.return_value = route = Mock(Route)
    route.getAction.return_value = action = MagicMock()
    action.return_value = response = Mock(HTTPResponse)

    resp = handle_http_request(request)

    router.find_route.assert_called_once_with('GET', '/welcome')
    route.getAction.assert_called_once_with()
    action.assert_called_once_with(request)
    assert resp == response

def test_handle_user_request():
    with patch.multiple('http.handle_requests',
                process_http_message=DEFAULT,
                handle_http_request=DEFAULT,
                handle_response=DEFAULT) as values:
        values['process_http_message'].return_value = request = Mock(HTTPRequest)
        values['handle_http_request'].return_value = response = Mock(HTTPResponse)
        handle_user_request('abc')
        values['process_http_message'].assert_called_once_with('abc')
        values['handle_http_request'].assert_called_once_with(request)
        values['handle_response'].assert_called_once_with(response)

def test_handle_user_request_with_exception():
    with patch.multiple('http.handle_requests',
                process_http_message=DEFAULT,
                handle_http_exception=DEFAULT,
                handle_response=DEFAULT) as values:
        values['process_http_message'].side_effect = e = BadRequestHttpException()
        values['handle_http_exception'].return_value = response = Mock(HTTPResponse)
        handle_user_request('abc')
        values['process_http_message'].assert_called_once_with('abc')
        values['handle_http_exception'].assert_called_once_with(e)
        values['handle_response'].assert_called_once_with(response)

def test_handle_http_response():
    response = Mock(HTTPResponse)
    response.status = 200
    response.code = 'OK'
    response.content_type = 'text/html'
    response.content_length = 1234
    response.content = '<html><body>hi</body></html>'
    value = handle_http_response(response)

    content_array = [
        'HTTP/1.1 200 OK',
        'Content-Type: text/html',
        'Content-Length: 1234',
        'Server: Ocean/0.1.1',
        '',
        '<html><body>hi</body></html>'
    ]
    assert value == '\n'.join(content_array)

