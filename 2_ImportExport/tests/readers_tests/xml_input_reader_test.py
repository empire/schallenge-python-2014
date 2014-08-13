__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


from readers import XMLInputReader
from transaction_commands import DepositCommand, WithdrawCommand, TransferCommand
import pytest
from mock import patch
import os

_open = open
def open(path):
    source_path = os.path.dirname(os.path.abspath(__file__))
    return _open(source_path + os.path.sep + path)

@pytest.fixture(scope="function", params=[
    ('data/deposit.xml',  [DepositCommand(3,  2.0), DepositCommand(7,  5.0)]),
    ('data/withdraw.xml',  [WithdrawCommand(13, 11.0), WithdrawCommand(19, 17.0)]),
    ('data/transfer.xml', [TransferCommand(2, 3, 5.0), TransferCommand(7, 11, 13.0)]),
])
def test_iter_args(request):
    return request.param
def test_iter(test_iter_args):
    reader = XMLInputReader()
    reader.open(open(test_iter_args[0]))

    commands = list(enumerate(reader))
    assert len(commands) == len(test_iter_args[1])
    for index, command in commands:
        assert type(test_iter_args[1][index]) == type(command)
        assert vars(test_iter_args[1][index]) == vars(command)