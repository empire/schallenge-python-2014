__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


from readers import JsonInputReader
from transaction_commands import DepositCommand, WithdrawCommand, TransferCommand
from mock import patch
import pytest

@patch('readers.json_input_reader.json')
def test_open(json_mock):
    reader = JsonInputReader()
    json_mock.load.return_value = 'sample output'
    assert reader._JsonInputReader__data == None
    reader.open(123)
    json_mock.load.assert_called_with(123)
    assert reader._JsonInputReader__data == 'sample output'


@pytest.fixture(scope="function", params=[
    ({'amount': 2.0,  'type': 'deposit',  'account_id': 3},      DepositCommand(3,  2)),
    ({'amount': 5.0,  'type': 'Withdraw',  'account_id': 7},     WithdrawCommand(7,  5)),
    ({'amount': 11.0, 'type': 'transfer', 'from': 13, 'to': 17}, TransferCommand(from_account=13, to_account=17, amount=11)),

])
def test_iter_args(request):
    return request.param

def test_iter(test_iter_args):
    reader = JsonInputReader()
    reader._JsonInputReader__data = dict(transactions=[test_iter_args[0]])
    iterator = iter(reader)
    n = iterator.next()
    assert type(n) == type(test_iter_args[1])
    assert vars(n) == vars(test_iter_args[1])
