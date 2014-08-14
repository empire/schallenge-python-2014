from http.exceptions.http_exception import NotFoundHttpException
from http.helpers.content_generator import handle_path, handle_file, handle_dir, generate_paths_index
from mock import patch, DEFAULT
import pytest
from tests.http_test import mock_http_response

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

@patch('http.helpers.content_generator.exists')
def test_generate_content_not_existence_resource(exists_mock):
    exists_mock.return_value = False
    with pytest.raises(NotFoundHttpException):
        handle_path('/server/avatar.jpg')
    exists_mock.assert_called_once_with('server/avatar.jpg')


def test_generate_content_not_existence_resource():
    with patch.multiple('http.helpers.content_generator',
            exists=DEFAULT, isdir=DEFAULT, handle_file=DEFAULT) as values:
        exists_mock = values['exists']
        isdir_mock = values['isdir']
        handle_file_mock = values['handle_file']
        exists_mock.return_value = True
        isdir_mock.return_value = False

        handle_path('/server/avatar.jpg', 1, 2)

        isdir_mock.assert_called_once_with('server/avatar.jpg')
        handle_file_mock.assert_called_once_with('server/avatar.jpg')

def test_generate_content_not_existence_resource():
    with patch.multiple('http.helpers.content_generator',
            exists=DEFAULT, isdir=DEFAULT, handle_dir=DEFAULT) as values:
        exists_mock = values['exists']
        isdir_mock = values['isdir']
        handle_dir_mock = values['handle_dir']
        exists_mock.return_value = True
        isdir_mock.return_value = True

        #Without first slash
        handle_path('server/avatar.jpg', 1, 2)

        isdir_mock.assert_called_once_with('server/avatar.jpg')
        handle_dir_mock.assert_called_once_with('server/avatar.jpg', 1, 2)

@patch('http.helpers.content_generator.bytes_from_file')
def test_handle_file(bytes_from_file_mock):
    bytes_from_file_mock.return_value = param = ['a', 'b', 'c', 'd']
    response = mock_http_response()

    content = handle_file('path/file.json', 1, response)

    bytes_from_file_mock.assert_called_once_with('path/file.json')
    assert None == content
    assert response.content == 'abcd'
    assert response.content_type == 'application/json'


@patch('http.helpers.content_generator.listdir')
def test_handle_dir(listdir):
    listdir.return_value = ['test.css', 'dir1', 'dir2/']
    with patch('http.helpers.content_generator.generate_paths_index') as generate_paths_index:
        response = mock_http_response()
        generate_paths_index.return_value = 'sample'

        handle_dir('base', None, response)

        listdir.assert_called_once_with('base')
        generate_paths_index.assert_called_once_with(['/base/test.css', '/base/dir1', '/base/dir2/'])
        assert response.content == 'sample'

def test_generate_paths_index():
    output = generate_paths_index(['/a/a.txt', 'b.txt', '/c', 'd', 'e/f'])
    assert output == '''<ul>
<li><a href="/a/a.txt">a.txt</a></li>
<li><a href="b.txt">b.txt</a></li>
<li><a href="/c">c</a></li>
<li><a href="d">d</a></li>
<li><a href="e/f">f</a></li>
<ul>
'''
