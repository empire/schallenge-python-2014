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
