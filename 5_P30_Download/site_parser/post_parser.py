__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


class CategoryPageParser:
    def __init__(self, soup):
        self.__soup = soup

    def get_post_links(self):
        for link in self.__soup.select('.post h1 a'):
            yield link.attrs['href']


    def get_pagination_pages(self):
        for link in self.__soup.select('.pagination li > a'):
            yield link.attrs['href']
