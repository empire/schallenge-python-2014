__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from output_writer import OutputWriter
import io


class TXTOutputWriter(OutputWriter):
    def __init__(self):
        pass

    def generate(self, data):
        output = io.StringIO()
        for account_info in data:
            output.write(str(account_info[0]) + u' ' +  str(account_info[1]) + '\n')

        value = output.getvalue()
        output.close()
        return value