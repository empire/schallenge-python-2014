from bs4 import BeautifulSoup

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def build_beautiful_soup(html_doc):
    soup = BeautifulSoup(html_doc, 'html5lib')
    print 'Page title: ', soup.find('title')
    return soup


def build_beautiful_soup_from_path(path):
    with open(path) as sample_pag:
        sample_content = ''.join(sample_pag.readlines())
        return build_beautiful_soup(sample_content)
