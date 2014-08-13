from lib.file_format_aware_container import FileFormatAwareContainer
from writers.json_output_writer import JSONOutputWriter
from writers.txt_output_writer import TXTOutputWriter
from writers.csv_output_writer import CSVOutputWriter
from writers.xml_output_writer import XMLOutputWriter


writer_container = FileFormatAwareContainer()

writer_container.register(JSONOutputWriter())
writer_container.register(TXTOutputWriter())
writer_container.register(CSVOutputWriter())
writer_container.register(XMLOutputWriter())

