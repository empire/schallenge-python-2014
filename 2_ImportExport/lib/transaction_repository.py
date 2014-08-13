__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


class TransactionRepository:
    def __init__(self):
        self.__accounts = {}


    def add_amount(self, account, count):
        self.__accounts[account] = self.get(account, 0) + count

repository = TransactionRepository()
