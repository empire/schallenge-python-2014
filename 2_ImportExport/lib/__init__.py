from lib.transaction_repository import TransactionRepository
from lib.path import extract_file_extension

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def _write_output(output_file, content):
    with open(output_file, 'w') as fp:
        fp.write(content)
