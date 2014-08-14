from http import router
from http.routing.route import Route

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


def hello_world(request, response):
    return 'hello world'

router.register_route(Route('GET', '/', hello_world))
