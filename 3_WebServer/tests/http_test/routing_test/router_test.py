from http.exceptions.http_exception import NotFoundHttpException
from http.routing.route import Route
from http.routing.router import Router
from mock import Mock
import pytest

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def test_find_route_not_found():
    router = Router()
    route = Mock(Route)
    route.matched.return_value = False
    router.register_route(route)
    with pytest.raises(NotFoundHttpException):
        router.find_route('GET', '/home')
    route.matched.assert_called_once_with('GET', '/home')

def test_find_route():
    router = Router()

    route = Mock(Route)
    route.matched.return_value = False

    route2 = Mock(Route)
    route2.matched.return_value = True
    router.register_route(route2)

    returned_route = router.find_route('GET', '/home')

    route.matched.assert_called_twice_with('GET', '/home')
    assert returned_route == route2

