from lib.file_format_aware_container import FileFormatAwareContainer
from mock import patch, Mock

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def test_container():
    format_aware = Mock()
    format_aware.supported_format.return_value = 'abc'

    container = FileFormatAwareContainer()
    assert not container.is_format_supported('abc')
    container.register(format_aware)
    format_aware.supported_format.assert_called_once_with()
    assert container.is_format_supported('abc')
    assert container.get('abc') == format_aware
