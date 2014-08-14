from http.exceptions.http_exception import HttpExceptionBase
from http.request_builder import process_http_message

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def handle_user_request(message):
    try:
        request = process_http_message(message)
        response = handle_http_request(request)
    except HttpExceptionBase, e:
        response = handle_http_exception(e)


def handle_http_request(request):
    return 1

def handle_http_exception(e):
    return 2
