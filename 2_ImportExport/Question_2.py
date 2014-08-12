__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

from readers import JsonInputReader, CSVInputReader, TXTInputReader

reader = TXTInputReader()
reader.open(open('samples/sample_input.txt'))

for command in reader:
    print command

reader.close()
