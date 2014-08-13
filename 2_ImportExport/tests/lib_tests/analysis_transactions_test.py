from lib.analysis_transactions import analysis_transactions
from lib.exceptions import FileFormatNotSupported
from mock import patch, DEFAULT, Mock
from pip import __main__
import pytest
from readers.input_reader import InputReader
from transaction_commands.transaction_command import TransactionCommand
from writers.output_writer import OutputWriter

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


@patch('lib.analysis_transactions.reader_container')
def test_invalid_input(reader_container):
    """

    :type reader_container: mock.Mock
    """
    reader_container.is_format_supported.return_value = False
    with pytest.raises(FileFormatNotSupported):
        analysis_transactions('input.txt', 'output.xml')
    reader_container.is_format_supported.assert_called_once_with('txt')

@patch('lib.analysis_transactions.reader_container')
def test_valid_input(reader_container):
    """

    :type reader_container: mock.Mock
    """
    builtin_open_patcher = patch('__builtin__.open')
    builtin_open_mock = builtin_open_patcher.start()
    builtin_open_mock.return_value = 123

    reader_container.is_format_supported.return_value = True
    reader_container.get.return_value = reader = Mock(InputReader)

    with patch.multiple('lib.analysis_transactions',
                _get_writer=DEFAULT,
                analysis_transactions_with_reader_writer=DEFAULT) as values:
        values['_get_writer'].return_value = writer = Mock(OutputWriter)
        analysis_transactions('input.txt', 'output.xml')
        values['_get_writer'].assert_called_once_with('output.xml')
        values['analysis_transactions_with_reader_writer'].assert_called_once_with(reader, writer)

    reader.open.assert_called_once_with(123)
    reader_container.is_format_supported.assert_called_once_with('txt')

    builtin_open_patcher.stop()

@patch('lib.analysis_transactions.writer_container')
def test_invalid_output(writer_container):
    """
    :type writer_container: mock.Mock
    """
    writer_container.is_format_supported.return_value = False
    with patch('lib.analysis_transactions._get_reader') as _get_reader:
        with pytest.raises(FileFormatNotSupported):
            analysis_transactions('input.txt', 'output.xml')
        _get_reader.assert_called_once_with('input.txt')

    writer_container.is_format_supported.assert_called_once_with('xml')


@patch('lib.analysis_transactions.writer_container')
def test_valid_output(writer_container):
    writer_container.is_format_supported.return_value = True
    writer_container.get.return_value = writer = Mock(OutputWriter)

    with patch.multiple('lib.analysis_transactions',
                _get_reader=DEFAULT,
                analysis_transactions_with_reader_writer=DEFAULT) as values:
        values['_get_reader'].return_value = reader = Mock(InputReader)
        analysis_transactions('input.txt', 'output.xml')
        values['_get_reader'].assert_called_once_with('input.txt')
        values['analysis_transactions_with_reader_writer'].assert_called_once_with(reader, writer)

    writer_container.is_format_supported.assert_called_once_with('xml')

def test_s():
    command1 = Mock(TransactionCommand)
    command2 = Mock(TransactionCommand)
    with patch.multiple('lib.analysis_transactions', _get_reader=DEFAULT, _get_writer=DEFAULT) as values:
        values['_get_reader'].return_value = [command1, command2]
        analysis_transactions('.txt', 'output.txt')
        command1.apply_to.assert_called_once_with_any()
        command2.apply_to.assert_called_once_with_any()
