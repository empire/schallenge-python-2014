from http import router
from http.routing.route import Route

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def bytes_from_file(filename):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(1024)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break

def hello_world(request, response):
    return 'hello world'

def show_pic(request, response):
    response.content_type = 'image/jpeg'

    return ''.join(bytes_from_file('web/assets/wikipedia-logo.jpg'))

router.register_route(Route('GET', '/', hello_world))
router.register_route(Route('GET', '/pic', show_pic))
