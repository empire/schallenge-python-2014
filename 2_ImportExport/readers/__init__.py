from lib.file_format_aware_container import FileFormatAwareContainer
from readers.json_input_reader import JsonInputReader
from readers.csv_input_reader import CSVInputReader
from readers.txt_input_reader import TXTInputReader
from readers.xml_input_reader import XMLInputReader

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


reader_container = FileFormatAwareContainer()
reader_container.register(JsonInputReader())
reader_container.register(CSVInputReader())
reader_container.register(TXTInputReader())
reader_container.register(XMLInputReader())
