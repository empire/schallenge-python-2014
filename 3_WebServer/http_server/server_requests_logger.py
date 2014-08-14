from datetime import datetime

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


class ServerRequestLogger:
    __logs = []

    def __init__(self):
        pass

    @classmethod
    def log(cls, request, response):
        print 'Connected with ' + request['client_ip'] + ':' + str(request['client_port'])
        log = ServerRequestLog(request['client_ip'], request['client_port'], datetime.now())
        log.request_path = request.path
        log.response_status = response.status
        cls.__logs.append(log)

    @classmethod
    def logs(cls):
        return cls.__logs[:]

class ServerRequestLog:
    def __init__(self, client_ip, client_port, connection_datetime):
        self.__client_ip = client_ip
        self.__client_port = client_port
        self.__connection_datetime = connection_datetime
        self.__request_path = None
        self.__response_status = None

    @property
    def client_ip(self):
        return self.__client_ip

    @property
    def client_port(self):
        return self.__client_port

    @property
    def connection_datetime(self):
        return self.__connection_datetime

    @property
    def request_path(self):
        return self.__request_path

    @request_path.setter
    def request_path(self, value):
        self.__request_path = value

    @property
    def response_status(self):
        return self.__response_status

    @response_status.setter
    def response_status(self, value):
        self.__response_status = value