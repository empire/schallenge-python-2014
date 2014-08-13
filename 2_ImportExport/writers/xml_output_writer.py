__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from output_writer import OutputWriter
from xml.etree.ElementTree import Element, SubElement, Comment, tostring


class XMLOutputWriter(OutputWriter):
    def __init__(self):
        pass

    def generate(self, data):
        root = Element('accounts_delta')
        for account_info in data:
            account = SubElement(root, 'account')
            id = SubElement(account, 'id')
            id.text = str(account_info[0])
            amount = SubElement(account, 'amount')
            amount.text = str(account_info[1])
        #
        #
        # field1 = SubElement(doc, "field1")
        # field1.set("name", "blah")
        # field1.text = "some value1"
        #
        # field2 = SubElement(doc, "field2")
        # field2.set("name", "asdfasd")
        # field2.text = "some vlaue2"

        return tostring(root, encoding='UTF-8')

        deltas = []
        for account_info in data:
            deltas.append(dict(account_id=account_info[0], amount=account_info[1]))

        return json.dumps(dict(accounts_delta=deltas))

