import json
import sys
import StringIO

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


class PostPageParser:
    def __init__(self):
        self.__soup = None

    @staticmethod
    def parser_factory(soup):
        soup_part = soup.select('#main-content')[0]
        parser = PostPageParser()
        parser.__soup = soup_part
        parser.base_soup = soup

        return parser

    @property
    def url(self):
        # Using find instead of select, for better performance
        return self.__soup.find('h1').find('a').attrs['href']

    @property
    def name(self):
        return self.__clean(self.__soup.find('h1').find('a').text)

    @property
    def views(self):
        # find first element that have hit css-class
        return self.__soup.find('', 'hit').text.split()[-1]

    @property
    def category(self):
        category_links = self.base_soup.find('', 'cat').find_all('a')
        return '/'.join(map(lambda tag: self.__clean(tag.text), category_links))

    @property
    def description(self):
        # Getting first paragraph
        p = self.base_soup.find('', 'post-content').find('p')

        # Next finding fist line break (br element)
        io = u''
        for element in p:
            if element.name == 'br':
                break
            # print >>io, element.text if hasattr(element, 'text') else element
            if hasattr(element, 'text'):
                io += element.text
            else:
                io += unicode(element)

        return self.__clean(io)

    @property
    def specification(self):
        spec_strong_tags = self.base_soup.find('', 'extra-info').find_all('strong')
        # print extra_info
        specification = {}
        value = key = ''
        for spec_strong_tag in spec_strong_tags:
            key = spec_strong_tag.text.split(':')[0]
            for tag in spec_strong_tag.next_siblings:
                if tag.name == 'strong' or tag.name == 'br':
                    specification[key] = self.__clean(value)
                    key = value = ''
                    break
                elif None == tag.name or 'img' == tag.name:
                    value += unicode(tag)
                else:
                    value += tag.text

        if key:
            specification[key] = self.__clean(value)
        return specification

    @property
    def download_links(self):
        """
        Getting download links, download links are located after img that contains
        'http://p30download.com/template/icons/set3/arrow-down.gif' src attribute

        In some pages like http://p30download.com/fa/entry/50159/ download links are not located in download-links,
           so if there is no img_tags I check all download links.
        """
        img_tags = self.base_soup.find('', 'download-links').find_all(src='http://p30download.com/template/icons/set3/arrow-down.gif')
        if not img_tags:
            img_tags = self.base_soup.find_all(src='http://p30download.com/template/icons/set3/arrow-down.gif')
        for img_tag in img_tags:
            a_tag = img_tag.findNext('a')
            yield a_tag.attrs['href']


    def jsonify(self):
        return json.dumps(
            {
                "name": self.name,
                "URL": self.url,
                "views": self.views,
                "category": self.category,
                "description": self.description,
                "specifications": self.specification,
                "download_links": list(self.download_links)
            }
        )


    def __clean(self, text):
        return ' '.join(text.split())

