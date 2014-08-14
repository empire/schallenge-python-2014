import StringIO
from http import router
from http.exceptions.http_exception import HttpExceptionBase
from http.http_response import HTTPResponse
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
    result = action(request, response)

    if None == result:
        response.status = 204
        response.content_type = 'text/html'
        response.content = ''

        return response
    if type(result) != str:
        return result

    response.content = result
    response.status = 200
    response.content_type = 'text/html'

    return response


def handle_http_exception(e):
    response = HTTPResponse()
    response.status = e.status
    response.code = e.message
    response.content_type = 'text/html'
    response.content = '<html><body>%d %s</body></html>'%(e.status, e.message,)
    return response
