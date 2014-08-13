from writers import XMLOutputWriter
from mock import patch
import pytest
from tests.writers_tests import sample_data
from xml.dom.minidom import parse, parseString

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


def test_generate():
    writer = XMLOutputWriter()
    output = writer.generate(sample_data)

    assert output == '''<?xml version='1.0' encoding='UTF-8'?>\n''' + \
    '''<accounts_delta>''' + \
    '''<account><id>1001</id><amount>2.0</amount></account>'''  + \
    '''<account><id>1002</id><amount>-3.0</amount></account>''' + \
    '''<account><id>1003</id><amount>0.0</amount></account>'''  + \
    '''<account><id>1004</id><amount>7.0</amount></account>'''  + \
    '''</accounts_delta>'''
