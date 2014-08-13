__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'

def extract_file_extension(file_name):
    """

    :type file_name: str
    """
    return '' if '.' not in file_name else file_name.lower().split('.')[-1]
