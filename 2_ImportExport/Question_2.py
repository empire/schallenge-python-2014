__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from readers import JsonInputReader, CSVInputReader

reader = CSVInputReader()
reader.open(open('samples/sample_input.csv'))

for command in reader:
    print command

reader.close()
