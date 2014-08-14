import StringIO
from http import router
from http.exceptions.http_exception import HttpExceptionBase
from http.http_request import HTTPRequest
from http.http_response import HTTPResponse
from http.request_builder import process_http_message
from http.routing.router import has_error_handler, error_handler, get_error_handler
from http_server.server_requests_logger import ServerRequestLogger

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def handle_user_request(message, *args, **kwargs):
    request = HTTPRequest()
    try:
        process_http_message(request, message, *args, **kwargs)
        response = handle_http_request(request)
    except HttpExceptionBase, e:
        response = handle_http_exception(request, e)

    ServerRequestLogger.log(request, response)
    return handle_response(response)

def handle_response(response):
    return handle_http_response(response)


def handle_http_response(response):
    io = StringIO.StringIO()
    print >>io, 'HTTP/1.1 %d %s' %(response.status, response.code)
    print >>io, 'Content-Type: %s' %(response.content_type,)
    print >>io, 'Content-Length: %d' %(response.content_length,)
    print >>io, 'Server: Ocean/0.1.1'
    print >>io, ''
    io.write(response.content)

    value = io.getvalue()
    io.close()

    return value

def handle_http_request(request):
    route = router.find_route(request.method, request.path)
    action = route.getAction()
    response = HTTPResponse()

    return handle_action(action, request, response)

def handle_action(action, request, response):
    result = action(request, response)

    if None == result:
        response.content = ''
    elif type(result) != str:
        return result
    else:
        response.content = result

    if None == response.status:
        response.status = 204 if None == result else 200

    if None == response.content_type:
        response.content_type = 'text/html'

    return response


def handle_http_exception(request, e):
    response = HTTPResponse()
    response.status = status = e.status
    response.code = e.message
    response.content_type = 'text/html'
    
    if has_error_handler(status):
        return handle_action(get_error_handler(status), request, response)
    
    response.content = '<html><body>%d %s</body></html>'%(e.status, e.message,)
    return response
