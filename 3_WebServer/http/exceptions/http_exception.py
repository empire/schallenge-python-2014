from exceptions import Exception

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


class HttpExceptionBase(Exception):
    def __init__(self, code, message):
        self.__code = code
        self.__message = message

class BadRequestHttpException(HttpExceptionBase):
    def __init__(self):
        HttpExceptionBase.__init__(self, 400, 'Bad Request')

class MethodNotAllowedHttpException(HttpExceptionBase):
    def __init__(self):
        HttpExceptionBase.__init__(self, 405, 'Method Not Allowed')

class NotImplementedHttpException(HttpExceptionBase):
    def __init__(self):
        HttpExceptionBase.__init__(self, 501, 'Not Implemented')

class NotFoundHttpException(HttpExceptionBase):
    def __init__(self):
        HttpExceptionBase.__init__(self, 404, 'Not Found')
