__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from output_writer import OutputWriter

import json

class JSONOutputWriter(OutputWriter):
    def __init__(self):
        pass

    def generate(self, data):
        deltas = []
        for account_info in data:
            deltas.append(dict(account_id=account_info[0], amount=account_info[1]))

        return json.dumps(dict(accounts_delta=deltas))

