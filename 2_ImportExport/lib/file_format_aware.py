__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


class FileFormatAware:
    def __init__(self):
        pass

    def supported_format(self):
        raise Exception('Must be implemented')
