import StringIO
import datetime
from http import router
from http.routing.route import Route
from server.server_requests_logger import ServerRequestLogger

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def hello_world(request, response):
    return 'hello world'

def show_pic(request, response):
    response.content_type = 'image/jpeg'

    return ''.join(bytes_from_file('web/assets/wikipedia-logo.jpg'))

def show_clients(request, response):
    def add_log_row(io, log):
        print >>io, '''
        <tr>
            <td>{index}</td>
            <td>{log.client_ip}</td>
            <td>{log.client_port}</td>
            <td>{log.request_path}</td>
            <td>{log.response_status}</td>
            <td>{log.connection_datetime}</td>
        </tr>'''.format(index=index, log=log)

    io = StringIO.StringIO()
    print >>io, '''<table border=1>
    <thead>
        <tr>
            <th>#</th>
            <th>IP</th>
            <th>Port</th>
            <th>Path</th>
            <th>Status</th>
            <th>Datetime</th>
        </tr>
    </thead>
    <tbody>'''
    for index, log in enumerate(ServerRequestLogger.logs()):
        add_log_row(io, log)

    print >>io, '</tbody></table>'

    return io.getvalue()

def my_aspx(request, response):
    io = StringIO.StringIO()

    print >>io, '<h1>Request Headers</h1>'
    print >>io, '<ul>'
    for header_item in request.headers.iteritems():
        print >>io, '<li>', ': '.join(header_item), '</li>'
    print >>io, '<li>IP: %s</li>'%request['client_ip']
    print >>io, '<li>PORT: %d</li>'%request['client_port']
    print >>io, '</ul>'

    return io.getvalue()

def time_php(request, response):
    io = StringIO.StringIO()

    print >>io, 'Server time: ', datetime.datetime.now(), '<hr />'
    print >>io, 'Host: ', request.headers['Host'].split(':')[0]
    return io.getvalue()

router.register_route(Route('GET', '/', hello_world))
router.register_route(Route('GET', '/pic', show_pic))
router.register_route(Route('GET', '/clients.html', show_clients))
router.register_route(Route('GET', '/my.aspx', my_aspx))
router.register_route(Route('GET', '/time.php', time_php))


def bytes_from_file(filename):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(1024)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break
