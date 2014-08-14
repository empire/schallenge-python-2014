import StringIO
from http import router
from http.exceptions.http_exception import HttpExceptionBase
from http.request_builder import process_http_message

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def handle_user_request(message):
    try:
        request = process_http_message(message)
        response = handle_http_request(request)
    except HttpExceptionBase, e:
        response = handle_http_exception(e)

    return handle_response(response)

def handle_response(response):
    return handle_http_response(response)


def handle_http_response(response):
    io = StringIO.StringIO()
    print >>io, 'HTTP/1.1 %d %s' %(response.status, response.code)
    print >>io, 'Content-Type: %s' %(response.content_type,)
    print >>io, 'Content-Length: %d' %(response.content_length,)
    print >>io, ''
    io.write(response.content)

    value = io.getvalue()
    io.close()

    return value

def handle_http_request(request):
    route = router.find_route(request.method, request.path)
    action = route.getAction()
    return action(request)


def handle_http_exception(e):
    return 2
