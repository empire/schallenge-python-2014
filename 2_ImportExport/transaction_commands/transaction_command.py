__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

class TransactionCommand:
    def __init__(self):
        pass

    def apply_to(self, repository):
        raise Exception('Must be implemented')
