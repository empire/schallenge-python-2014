from exceptions import Exception

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


class HttpExceptionBase(Exception):
    def __init__(self, status, message):
        self.__status = status
        self.__message = message

    @property
    def status(self):
        return self.__status

    @property
    def message(self):
        return self.__message

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
