__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from input_reader import InputReader
from transaction_commands import DepositCommand, PaymentCommand, TransferCommand

_command_factories = dict(
    deposit  = lambda data: DepositCommand(int(data[1]), float(data[2])),
    payment  = lambda data: PaymentCommand(int(data[1]), float(data[2])),
    transfer = lambda data: TransferCommand(int(data[1]), int(data[4]), float(data[2])),
)

class TXTInputReader(InputReader):
    def __init__(self):
        self.__data = None

    def open(self, fp):
        self.__data = fp

    def __iter__(self):
        class Iterator:
            def __init__(self, data):
                self.__data_iter = data

            def next(self):
                row = self.__data_iter.next().strip()
                """
                :type row: str
                """
                row_data = filter(lambda x: x, row.split(' '))
                row_type = self.__get_type(row_data)
                return _command_factories[row_type](row_data)
            def __get_type(self, row_data):
                """
                :type row_data: list
                """
                if row_data[0] == 'Deposit':
                    return 'deposit'
                elif row_data[0] == 'Payment':
                    return 'payment'
                return 'transfer'

        return Iterator(self.__data)

    def supported_format(self):
        return 'txt'

    def close(self):
        pass
