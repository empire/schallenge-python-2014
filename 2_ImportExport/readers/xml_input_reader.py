__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from input_reader import InputReader
from transaction_commands import DepositCommand, PaymentCommand, TransferCommand

from xml.dom import minidom

from xml.sax import ContentHandler, make_parser, handler

class TransactionHandler(ContentHandler):
    __main_tags = set(['deposit', 'transactions', 'payment', 'transfer'])
    def __init__(self):
        self.__data = {}
        self.commands = []

        self.__current_tag = ''
        self.__content = ''

    # Call when an element starts
    def startElement(self, tag, attributes):
        self.__current_tag = tag
        if tag in self.__main_tags:
            self.__data = {}
            return

        assert tag in ['account_id', 'amount', 'from', 'to']

    def endElement(self, tag):
        if 'transactions' == tag:
            pass
        elif 'deposit' == tag:
            self.commands.append(DepositCommand(int(self.__data['account_id']), float(self.__data['amount'])))
        elif 'payment' == tag:
            self.commands.append(PaymentCommand(int(self.__data['account_id']), float(self.__data['amount'])))
        elif 'transfer' == tag:
            self.commands.append(TransferCommand(int(self.__data['from']), int(self.__data['to']), float(self.__data['amount'])))
        else:
            self.__data[self.__current_tag] = self.__content
            self.__content = ''
            # assert tag in ['account_id', 'amount'] or self.__data == 1

    def characters(self, content):
        content = content.strip()
        if self.__current_tag in self.__main_tags:
            return

        self.__content += content

class XMLInputReader(InputReader):
    def __init__(self):
        pass

    def open(self, fp):
        parser = make_parser()
        parser.setFeature(handler.feature_namespaces, 0)
        transaction_handler = TransactionHandler()
        parser.setContentHandler(transaction_handler)
        parser.parse(fp)

        self.__commands = transaction_handler.commands

    def __iter__(self):
        return iter(self.__commands)

    def supported_format(self):
        return 'xml'

    def close(self):
        pass
