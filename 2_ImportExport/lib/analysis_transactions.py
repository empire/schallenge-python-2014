from lib import transaction_repository
from lib.exceptions import FileFormatNotSupported
from lib.path import extract_file_extension
from lib.transaction_repository import repository
from readers import reader_container
from readers.input_reader import InputReader
from writers import writer_container

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


def analysis_transactions(input_file, output_file):
    reader = _get_reader(input_file)
    writer = _get_writer(output_file)sdfa

    analysis_transactions_with_reader_writer(reader, writer)

def analysis_transactions_with_reader_writer(reader, writer):
    for command in reader:
        command.apply_to(repository)
    transactions = repository.get_formatted_transactions()
    return writer.generate(transactions)

def _get_reader(input_file):
    """
    :rtype : readers.input_reader.InputReader
    """
    input_file_extension = extract_file_extension(input_file)
    if not reader_container.is_format_supported(input_file_extension):
        raise FileFormatNotSupported(input_file)

    reader = reader_container.get(input_file_extension)
    assert isinstance(reader, InputReader)
    reader.open(open(input_file))

    return reader

def _get_writer(output_file):
    """
    :rtype : writers.output_writer.OutputWriter
    """
    output_file_extension = extract_file_extension(output_file)
    if not writer_container.is_format_supported(output_file_extension):
        raise FileFormatNotSupported(output_file)

    return writer_container.get(output_file_extension)
