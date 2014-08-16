# -*- coding: utf-8 -*-
import json
from mock import patch, DEFAULT
from site_parser.category_parser import CategoryPageParser
from site_parser.helpers import build_beautiful_soup_from_path
from site_parser.post_parser import PostPageParser

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


def test_get_post_href():
    soup = build_beautiful_soup_from_path('sample/sample_post.html')
    post = PostPageParser.parser_factory(soup)

    url = 'http://p30download.com/fa/entry/35912/'
    name = u'دانلود Ubuntu v14.04.1 x86/x64 - لینوکس اوبونتو'
    views = '217,150'
    category = u'نرم افزار/سیستم عامل/لینوکس'
    description = u'''Ubuntu نمونه توضیح کوتاه شده برات تست بهتر'''
    specifications = {
        u'امتیاز': '<img class="image-middle" src="http://p30download.com/template/images/4.5-star.gif"/>',
        u'تاریخ انتشار': '09:59 - 93/5/12',
        u'حجم فایل': u'753.3 + 763 مگابایت',
        u'منبع': u'پی سی دانلود',
    }
    download_links = [
        'http://ftp.ticklers.org/releases.ubuntu.org/releases//14.04.1/ubuntu-14.04.1-desktop-i386.iso',
        'http://ftp.acc.umu.se/mirror/ubuntu-releases/14.04.1/ubuntu-14.04.1-desktop-amd64.iso',
    ]
    assert post.url == url
    assert post.name == name
    assert post.views == views
    assert post.category == category
    assert post.description == description
    assert post.specification == specifications
    assert list(post.download_links) == download_links

    assert json.loads(post.jsonify()) == {
        'URL': url,
        'name': name,
        'views': views,
        'category': category,
        'description': description,
        'specifications': specifications,
        'download_links': download_links,
    }
