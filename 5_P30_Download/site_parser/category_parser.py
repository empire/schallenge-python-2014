__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


class CategoryPageParser:
    def __init__(self, soup):
        self.__soup = soup

    def get_post_links(self):
        for link in self.__soup.select('.post h1 a'):
            href = link.attrs['href']
            if '://p30download.com/' not in href:
                continue
            yield href


    def get_pagination_pages(self):
        pagination = self.__soup.select('.pagination li > a')
        links = []
        for link in pagination:
            link = link.attrs['href']
            # Ignore duplicated links(link-to last/first page may be duplicated)
            if link not in links:
                links.append(link)
        return links