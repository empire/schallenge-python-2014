__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


class HTTPResponse:
    def __init__(self):
        self.__status = 'GET'
        self.__content = None
        self.__content_type = None

    @property
    def status(self):
        return self.__status

    @status.setter
    def status(self, status):
        self.__status = status

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, content):
        self.__content = content

    @property
    def content_type(self):
        return self.__content_type

    @content_type.setter
    def content_type(self, content_type):
        self.__content_type = content_type

    @property
    def code(self):
        return http_codes[self.status]

    @property
    def content_length(self):
        return len(self.content)

http_codes = {
    200: 'OK'
}
