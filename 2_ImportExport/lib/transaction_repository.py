__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from sortedcontainers import SortedDict
class TransactionRepository:
    def __init__(self):
        self.__accounts = SortedDict()

    def add_amount(self, account, amount):
        account = int(account)
        amount = float(amount)
        self.__accounts[account] = self.__accounts.get(account, 0) + float(amount)

    def get_account_amount(self, account):
        return self.__accounts[int(account)]

    def get_formatted_transactions(self):
        return self.__accounts.iteritems()

    def clear(self):
        self.__accounts.clear()

repository = TransactionRepository()
