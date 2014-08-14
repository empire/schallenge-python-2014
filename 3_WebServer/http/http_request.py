__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

class HTTPRequest(object):
    def __init__(self):
        self.__method = 'GET'
        self.__path = None
        self.__headers = None

    @property
    def method(self):
        return self.__method

    @method.setter
    def method(self, method):
        self.__method = method

    @property
    def path(self):
        return self.__path

    @path.setter
    def path(self, path):
        self.__path = path

    @property
    def headers(self):
        return self.__headers

    @headers.setter
    def headers(self, headers):
        self.__headers = headers

    def set_server_kwargs(self, **kwargs):
        self.__server_kwargs = kwargs

    def __getitem__(self, item):
        return self.__server_kwargs[item]
