"""
JSON logger
"""

from datetime import datetime
import json

TRACE = 0
DEBUG = 1
INFO = 2
WARN = 3
ERROR = 4


class Logger:
    def __init__(self, level):
        self._min_level = self.__level_int(level)
        self._extra_data = {}

    def extra(self, key=None, value=None, map=None):
        if map:
            self._extra_data.update(map)
        elif key and value:
            self._extra_data[key] = value
        return self

    def trace(self):
        new = Logger(self.__level_str(self._min_level))
        new._level = TRACE
        return new

    def debug(self):
        new = Logger(self.__level_str(self._min_level))
        new._level = DEBUG
        return new

    def info(self):
        new = Logger(self.__level_str(self._min_level))
        new._level = INFO
        return new

    def warn(self):
        new = Logger(self.__level_str(self._min_level))
        new._level = WARN
        return new

    def error(self):
        new = Logger(self.__level_str(self._min_level))
        new._level = ERROR
        return new

    def msg(self, msg):
        if self._min_level > self._level:
            return
        entry = {
            'time': datetime.now().isoformat(),
            'level': self.__level_str(self._level),
        }
        entry.update(self._extra_data)
        entry['message'] = msg
        print(json.dumps(entry))

    def __level_str(self, level):
        if level == TRACE:
            return "TRACE"
        if level == DEBUG:
            return "DEBUG"
        if level == INFO:
            return "INFO"
        if level == WARN:
            return "WARNING"
        if level == ERROR:
            return "ERROR"
        return "INFO"

    def __level_int(self, level):
        if level == "TRACE":
            return TRACE
        if level == "DEBUG":
            return DEBUG
        if level == "INFO":
            return INFO
        if level == "WARNING":
            return WARN
        if level == "ERROR":
            return ERROR
        return INFO
