import mimetypes
import StringIO
from os import listdir
from http.exceptions.http_exception import NotFoundHttpException
import os

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from os.path import exists, isdir


def handle_path(path, request, response):
    if path.startswith('/'):
        path = path[1:]

    if not exists(path):
        raise NotFoundHttpException()

    [handle_file, handle_dir][isdir(path)](path, request, response)

def handle_file(path, request, response):
    content = ''.join(bytes_from_file(path))
    response.content = content
    response.content_type = mimetypes.guess_type(path)[0]

def handle_dir(path, request, response):
    formatted_path = path
    if not path.startswith('/'):
        formatted_path = '/' + path
    formatted_path += '/'
    paths = []
    for name in listdir(path):
        paths.append(formatted_path + name)
    response.content = generate_paths_index(paths)

def generate_paths_index(paths):
    io = StringIO.StringIO()
    print >>io, '<ul>'
    for path in paths:
        print >>io, '<li><a href="{0}">{1}</a></li>'.format(path,  os.path.basename(path))
    print >>io, '<ul>'

    return io.getvalue()

def bytes_from_file(filename):
    with open(filename, "rb") as f:
        while True:
            chunk = f.read(1024)
            if chunk:
                for b in chunk:
                    yield b
            else:
                break
