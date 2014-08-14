from http.exceptions.http_exception import BadRequestHttpException, MethodNotAllowedHttpException, \
    NotImplementedHttpException
from http.http_request import HTTPRequest

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

__supported_methods = ['GET']

def process_http_message(request, message, *args, **kwargs):
    set_request_kwargs(request, **kwargs)
    message_parts = message.replace('\r\n', '\n').split('\n\n')

    if len(message_parts) == 1:
        header, content = message_parts[0], ''
    else:
        header, content = message_parts[:2]

    lines = header.split('\n')
    initial_line = lines[0]
    method, path, protocol = parse_initial_line(initial_line)
    build_request(request, method, path)
    set_request_headers(request, filter(lambda x:x, lines[1:]))
    _check_method(method)

def _check_method(method):
    if method not in __supported_methods:
        # as mentioned in question, must return 405 instead of 501!
        # raise NotImplementedHttpException()
        raise MethodNotAllowedHttpException()

def parse_headers(headers):
    header_bag = dict()
    for header in headers:
        header_parts = header.split(':')
        if len(header_parts) <= 1:
            raise BadRequestHttpException()
        header_bag[header_parts[0].strip()] = ':'.join(header_parts[1:]).strip()

    return header_bag

def set_request_headers(request, headers):
    headers_dict = parse_headers(headers)
    if 'Host' not in headers_dict:
        raise BadRequestHttpException()
    request.headers = headers_dict

def set_request_kwargs(request, **kwargs):
    request.set_server_kwargs(**kwargs)

def build_request(request, method, path):
    request.method = method
    request.path = path

    return request

def parse_initial_line(initial_line):
    initial_line_parts = initial_line.split(' ')
    method = initial_line_parts[0]

    path = None
    protocol = None
    parts_count = len(initial_line_parts)
    if parts_count == 1:
        pass
    elif parts_count == 2:
        path = initial_line_parts[1]
    else:
        path = ' '.join(initial_line_parts[1:-1])
        protocol = initial_line_parts[-1]

    return method, path, protocol
