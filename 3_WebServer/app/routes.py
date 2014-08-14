import StringIO
import datetime
from http import router
from http.helpers.content_generator import handle_file, handle_path
from http.routing.route import Route
from http.routing.router import error_handler
from http_server.server_requests_logger import ServerRequestLogger

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def hello_world(request, response):
    return 'hello world'

def show_pic(request, response):
    return handle_file('web/assets/wikipedia-logo.jpg', request, response)

def show_clients(request, response):
    return get_clients_html(request, response, ServerRequestLogger.logs())

def get_clients_html(request, response, logs):
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
    for index, log in enumerate(logs):
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

def server_show(request, response):
    path = request.path[1:]
    return handle_path(path, request, response)

router.register_route(Route('GET', '/', hello_world))
router.register_route(Route('GET', '/pic', show_pic))
router.register_route(Route('GET', '/clients.html', show_clients))
router.register_route(Route('GET', '/my.aspx', my_aspx))
router.register_route(Route('GET', '/time.php', time_php))
router.register_route(Route('GET', '/server', server_show))
router.register_route(Route('GET', '/server/.*', server_show))

@error_handler(404)
def handler_404(request, response):
    return '''
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html>
    <head>
        <title>404 Not Found</title>
    </head>
    <body>
        <h1>Not Found</h1>
        <p>The requested URL <b>{request.path}</b> was not found on this server.</p>
        <hr>
        <address>Ocean/0.1.1</address>
    </body>
</html>
    '''.format(request=request)

@error_handler(501)
@error_handler(405)
def handler_501(request, response):
    # Just show logs related ot port 8181 as mention in question
    logs = filter(lambda log: log.client_port == 8181, ServerRequestLogger.logs())
    return '''
<!DOCTYPE HTML PUBLIC "-//IETF//DTD HTML 2.0//EN">
<html>
    <head>
        <title>Method Not allowed</title>
    </head>
    <body>
        <h1>Method Not allowed</h1>
        <p>The requested <b>{request.method}</b> for {request.path} was not allowed on this server.</p>
        <hr>
        {log}
        <hr>
        <address>Ocean/0.1.1</address>
    </body>
</html>
    '''.format(request=request, log=get_clients_html(request, response))

