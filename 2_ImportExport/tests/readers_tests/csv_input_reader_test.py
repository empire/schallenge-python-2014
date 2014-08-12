__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


from readers import CSVInputReader
from transaction_commands import DepositCommand, PaymentCommand, TransferCommand
from mock import patch
import pytest

@patch('readers.csv_input_reader.csv')
def test_open(csv_mock):
    reader = CSVInputReader()
    csv_mock.reader.return_value = iter([[' From ', ' To', ' Amount'], ['2', '3', '5']])
    assert reader._CSVInputReader__data == None
    reader.open(123)
    csv_mock.reader.assert_called_with(123)
    assert reader._CSVInputReader__head == ['from', 'to', 'amount']
    assert next(reader._CSVInputReader__data) == ['2', '3', '5']


@pytest.fixture(scope="function", params=[
    (['', 3,  2],  DepositCommand(3,  2)),
    ([7,  '', 5],  PaymentCommand(7,  5)),
    ([13, 17, 11], TransferCommand(from_account=13, to_account=17, amount=11)),
])
def test_iter_args(request):
    return request.param

def test_iter(test_iter_args):
    reader = CSVInputReader()
    reader._CSVInputReader__head = ['from', 'to', 'amount']
    reader._CSVInputReader__data = iter([test_iter_args[0]])
    iterator = iter(reader)
    n = iterator.next()
    assert type(n) == type(test_iter_args[1])
    assert vars(n) == vars(test_iter_args[1])
