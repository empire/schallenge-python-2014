from lib.analysis_transactions import analysis_transactions

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

analysis_transactions('samples/sample_input.csv', '/tmp/generated_output.xml')
analysis_transactions('samples/sample_input.xml', '/tmp/generated_output.csv')