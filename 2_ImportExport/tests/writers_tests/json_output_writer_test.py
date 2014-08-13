__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from mock import patch
import pytest
from tests.writers_tests import sample_data

from writers import JSONOutputWriter
import json

def test_generate():
    writer = JSONOutputWriter()
    output = writer.generate(sample_data)
    assert json.loads(output) == json.loads('''
        {
            "accounts_delta":
            [
                {"amount": 2.0, "account_id": 1001},
                {"amount": -3.0, "account_id": 1002},
                {"amount": 0.0, "account_id": 1003},
                {"amount": 7.0, "account_id": 1004}
            ]
        }''')
