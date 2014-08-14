from http.exceptions.http_exception import BadRequestHttpException, MethodNotAllowedHttpException, \
    NotImplementedHttpException
from http.http_request import HTTPRequest

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


def process_http_message(msg):
    lines = msg.split('\r\n')
    initial_line = lines[0]
    method, path, protocol = parse_initial_line(initial_line)
    request = build_request(method, path)
    set_request_headers(request, filter(lambda x:x, lines[1:]))

    return request

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

def build_request(method, path):
    request = HTTPRequest()
    request.method = method
    request.path = path

    return request

__supported_methods = ['GET']

def parse_initial_line(initial_line):
    initial_line_parts = initial_line.split(' ')
    method = initial_line_parts[0]
    if method not in __supported_methods:
        raise NotImplementedHttpException()

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
