__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from transaction_command import TransactionCommand
from lib import TransactionRepository

class TransferCommand(TransactionCommand):
    def __init__(self, from_account, to_account, amount):
        self.__from_account = from_account
        self.__to_account = to_account
        self.__amount = amount

    def apply_to(self, repository):
        """
        :type repository: TransactionRepository
        """
        repository.add_count(self.__from_account, -self.__amount)
        repository.add_count(self.__to_account,    self.__amount)
