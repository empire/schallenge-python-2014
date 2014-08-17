from lib.transaction_sorter import sort_transactions

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

file_names = map(lambda x: 'large_files_samples/' + x,
         ['1.csv', '2.csv', '3.csv', '4.csv', '5.csv', '6.csv', '7.csv', '8.csv', '9.csv', '10.csv']
)

sort_transactions(file_names, 'out/large_files_generated')
