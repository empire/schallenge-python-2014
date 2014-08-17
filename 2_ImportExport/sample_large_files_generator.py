import random

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

# Choosing Prime number
lowest_account_number = 2
highest_account_number = 104729
lowest_amount = 2

def deposit_csv_generator():
    amount = lowest_amount
    for acc in xrange(lowest_account_number, highest_account_number + 1):
        yield ('', acc, amount)
        amount += 1

def withdraw_csv_generator():
    amount = lowest_amount
    for acc in xrange(lowest_account_number, highest_account_number + 1):
        yield (acc, '', amount)
        amount += 1

def transfer_csv_generator():
    amount = lowest_amount
    top = lowest_account_number + highest_account_number
    for acc in xrange(lowest_account_number, highest_account_number + 1):
        yield (acc, top-acc, amount)
        amount += 1

generators = [
    deposit_csv_generator(),
    withdraw_csv_generator(),
    transfer_csv_generator()
]

def row_generator():
    while generators:
        generator = random.choice(generators)
        try:
            yield next(generator)
        except StopIteration:
            generators.remove(generator)


f = None
rows_per_file = (highest_account_number - lowest_account_number)/ 3
for i, row in enumerate(row_generator()):
    if i % rows_per_file == 0:
        if f != None:
            f.close()
        f = open('large_files_samples/%d.csv'%(i / rows_per_file + 1), 'w')
        print >>f, ','.join(['From', 'To', 'Amount'])
    print >>f, ','.join(map(str, row))
f.close()
