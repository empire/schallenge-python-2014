from lib.file_format_aware import FileFormatAware

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


class InputReader(FileFormatAware):
    def __iter__(self):
        raise Exception('Must be implemented')

    def open(self, fp):
        raise Exception('Must be implemented')
