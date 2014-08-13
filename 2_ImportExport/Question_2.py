from lib.analysis_transactions import analysis_transactions
from lib.transaction_repository import repository

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

analysis_transactions('samples/sample_input.csv', '/tmp/generated_output.csv')
repository.clear()
analysis_transactions('samples/sample_input.xml', '/tmp/generated_output.xml')
repository.clear()
analysis_transactions('samples/sample_input.json', '/tmp/generated_output.json')
repository.clear()
analysis_transactions('samples/sample_input.txt', '/tmp/generated_output.txt')