__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from mock import patch
import pytest
from tests.writers_tests import sample_data

from writers import TXTOutputWriter

import json

def test_generate():
    writer = TXTOutputWriter()
    output = writer.generate(sample_data)
    assert output == '''1001 2.0\n1002 -3.0\n1003 0.0\n1004 7.0\n'''
