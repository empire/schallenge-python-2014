from http.routing.route import Route

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def test_matched_different_method():
    assert not Route('GET', '/', lambda x:x).matched('POST', '/')
    assert not Route('GET', '/hello', lambda x:x).matched('POST', '/hello')

def test_matched_different_path():
    assert not Route('GET', '/', lambda x:x).matched('GET', '/hello')
    assert not Route('GET', '/hello', lambda x:x).matched('GET', '/')

def test_matched_similar_path_name():
    assert not Route('GET', '/', lambda x:x).matched('GET', '/hello')
    assert not Route('GET', '/hello', lambda x:x).matched('GET', '/hell')
    assert not Route('GET', '/hello', lambda x:x).matched('GET', '/helloo')
    assert not Route('GET', '/hello', lambda x:x).matched('GET', 'helloo')
    assert not Route('GET', '/hello', lambda x:x).matched('GET', 'hello/o')
    assert not Route('GET', '/hello', lambda x:x).matched('GET', 'hello')
    assert not Route('GET', '/hello', lambda x:x).matched('GET', 'hello/')
    assert not Route('GET', '/hello', lambda x:x).matched('GET', '.*')

def test_matched_simple_path():
    assert Route('GET', '', lambda x:x).matched('GET', '')
    assert Route('GET', '/pic', lambda x:x).matched('GET', '/pic')
    assert Route('GET', '/time.php', lambda x:x).matched('GET', '/time.php')
    assert Route('GET', '/welcome', lambda x:x).matched('GET', '/welcome?id=1')
    assert Route('GET', '/welcome', lambda x:x).matched('GET', '/welcome#link')

def test_matched_pattern_path():
    assert Route('GET', '/pi.*', lambda x:x).matched('GET', '/pic')
    assert Route('GET', '/server/.*', lambda x:x).matched('GET', '/server/avatar.png')
    assert Route('GET', '/server/.*', lambda x:x).matched('GET', '/server/assets/avatar.png')
    assert Route('GET', '.*', lambda x:x).matched('GET', '/server/assets/avatar.png')
    assert Route('GET', '.*', lambda x:x).matched('GET', '/index.php')
    assert Route('GET', '.*', lambda x:x).matched('GET', 'welcome.php')

