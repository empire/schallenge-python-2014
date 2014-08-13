__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from input_reader import InputReader
from transaction_commands import DepositCommand, WithdrawCommand, TransferCommand

import csv

_command_factories = dict(
    deposit  = lambda data: DepositCommand(int(data['to']), float(data['amount'])),
    withdraw  = lambda data: WithdrawCommand(int(data['from']), float(data['amount'])),
    transfer = lambda data: TransferCommand(int(data['from']), int(data['to']), float(data['amount'])),
)

class CSVInputReader(InputReader):
    def __init__(self):
        self.__data = None
        self.__head = None

    def open(self, fp):
        self.__data = csv.reader(fp)
        head = map(str.strip, next(self.__data))
        head = map(str.lower, head)
        self.__head = head

    def __iter__(self):
        class Iterator:
            def __init__(self, head, data):
                self.__head = head
                self.__data_iter = data

            def next(self):
                row = self.__data_iter.next()
                row_dict = dict(zip(self.__head, row))
                row_type = self.__get_type(row_dict)
                return _command_factories[row_type](row_dict)
            def __get_type(self, dict_row):
                """
                :type dict_row: dict
                """
                if dict_row['from'] == '':
                    return 'deposit'
                elif dict_row['to'] == '':
                    return 'withdraw'
                return 'transfer'

        return Iterator(self.__head, self.__data)

    def supported_format(self):
        return 'csv'

    def close(self):
        pass
