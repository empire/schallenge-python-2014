from bs4 import BeautifulSoup

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def build_beautiful_soup(html_doc):
    return BeautifulSoup(html_doc)


def build_beautiful_soup_from_path(path):
    with open(path) as sample_pag:
        sample_content = ''.join(sample_pag.readlines())
        return build_beautiful_soup(sample_content)
