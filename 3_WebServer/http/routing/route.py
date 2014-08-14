import re

__author__ = 'Hossein Zolfi <hossein.zolfi@gmail.com>'


class Route:
    def __init__(self, method, pattern, action):
        self.__method = method
        self.__pattern_compiled = re.compile('^%s$'%pattern)
        self.__action = action

    def getAction(self):
        return self.__action


    def matched(self, method, path):
        if method != self.__method:
            return False

        if self.__pattern_compiled.match(path):
            return True

        return False
