from lib.file_format_aware import FileFormatAware

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


class OutputWriter(FileFormatAware):
    def __init__(self):
        pass

    def generate(self, data):
        raise Exception('Must be implemented')