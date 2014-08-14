from http.exceptions.http_exception import NotFoundHttpException

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


class Router:
    def __init__(self):
        self.__routes = []

    def find_route(self, method, path):
        for route in self.__routes:
            if route.matched(method, path):
                return route

        raise NotFoundHttpException()

    def register_route(self, route):
        self.__routes.append(route)

__error_handlers = dict()
def error_handler(code):
    def decorator(fnc):
        __error_handlers[code] = fnc
        def wrapper(*args, **kws):
            return fnc(*args, **kws)
        return wrapper
    return decorator


def has_error_handler(code):
    return code in __error_handlers


def get_error_handler(code):
    return __error_handlers[code]
