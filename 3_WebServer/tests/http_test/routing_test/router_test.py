from http.exceptions.http_exception import NotFoundHttpException
from http.routing.route import Route
from http.routing.router import Router, has_error_handler, error_handler, get_error_handler
from mock import Mock, MagicMock
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

def test_error_handler():
    assert not has_error_handler(404)
    handler = MagicMock()
    error_handler(404)(handler)
    assert has_error_handler(404)

    handler.return_value = 123
    assert get_error_handler(404)(1, 2, key='value') == 123
    handler.assert_called_once_with(1, 2, key='value')
