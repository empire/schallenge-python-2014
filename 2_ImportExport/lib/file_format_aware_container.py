__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


class FileFormatAwareContainer:
    def __init__(self):
        self.__formats = {}

    def register(self, format_aware):
        """
        :type format_aware: lib.file_format_aware.FileFormatAware
        :param format_aware:
        """
        self.__formats[format_aware.supported_format()] = format_aware

    def get(self, file_format):
        return self.__formats[file_format]

    def is_format_supported(self, file_format):
        return self.__formats.has_key(file_format)
