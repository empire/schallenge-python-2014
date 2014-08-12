__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from input_reader import InputReader
from transaction_commands import DepositCommand, PaymentCommand, TransferCommand

import json

_command_factories = dict(
    deposit  = lambda data: DepositCommand(data['account_id'], data['amount']),
    payment  = lambda data: PaymentCommand(data['account_id'], data['amount']),
    transfer = lambda data: TransferCommand(data['from'], data['to'], data['amount']),
)

class JsonInputReader(InputReader):
    def __init__(self):
        self.__data = None

    def open(self, fp):
        self.__data = json.load(fp)

    def __iter__(self):
        class Iterator:
            def __init__(self, data):
                self.__data_iter = iter(data['transactions'])

            def next(self):
                data = self.__data_iter.next()
                return _command_factories[data['type']](data)

        return Iterator(self.__data)

    def close(self):
        pass
