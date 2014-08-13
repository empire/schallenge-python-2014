__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


from readers import TXTInputReader
from transaction_commands import DepositCommand, WithdrawCommand, TransferCommand
import pytest

def test_open():
    reader = TXTInputReader()
    assert reader._TXTInputReader__data == None
    reader.open(123)
    assert reader._TXTInputReader__data == 123


@pytest.fixture(scope="function", params=[
    ('  Deposit   3    2.0  \r\f\n',  DepositCommand(3,  2)),
    ('Deposit  3  2.0\n',       DepositCommand(3,  2)),
    ('Withdraw  7  5.0\n',      WithdrawCommand(7,  5)),
    ('Transfer 13 11.0 > 17\n', TransferCommand(from_account=13, to_account=17, amount=11)),
])
def test_iter_args(request):
    return request.param

def test_iter(test_iter_args):
    reader = TXTInputReader()
    reader._TXTInputReader__data = iter([test_iter_args[0]])
    iterator = iter(reader)
    n = iterator.next()
    assert type(n) == type(test_iter_args[1])
    assert vars(n) == vars(test_iter_args[1])
