from lib.path import extract_file_extension

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


def test_extract_file_extension():
    assert extract_file_extension('') == ''
    assert extract_file_extension('text') == ''
    assert extract_file_extension('.text') == 'text'
    assert extract_file_extension('a.b.c.text') == 'text'
    assert extract_file_extension('a.b.c.TeXt') == 'text'
    assert extract_file_extension('a/b/c.d.TeXt') == 'text'
