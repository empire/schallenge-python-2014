__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

class TransactionCommand:
    def __init__(self):
        pass

    def apply_to(self, repository):
        raise Exception('Must be implemented')

    @property
    def order(self):
        raise Exception('Must be implemented')

    def __lt__(self, other):
        delta = other.order - self.order
        if delta != 0:
            return delta < 0
        return self.amount - other.amount < 0

    def __le__(self, other):
        delta = other.order - self.order
        if delta != 0:
            return delta < 0
        return self.amount - other.amount <= 0

    def __gt__(self, other):
        delta = other.order - self.order
        if delta != 0:
            return delta > 0
        return self.amount - other.amount > 0

    def __ge__(self, other):
        delta = other.order - self.order
        if delta != 0:
            return delta > 0
        return self.amount - other.amount >= 0

    def __eq__(self, other):
        if not isinstance(other, TransactionCommand):
            return False

        delta = other.order - self.order
        if delta != 0:
            return False
        return self.amount == other.amount

    def __ne__(self, other):
        if not isinstance(other, TransactionCommand):
            return True

        delta = other.order - self.order
        if delta != 0:
            return True
        return self.amount != other.amount
