from dataclasses import dataclass
from typing import Optional


@dataclass
class Logger:
    """ Singleton logging class that has been set up only once during first instantiation.

    Each further instantiation does not change the settings.
    """
    @dataclass
    class __Logger:
        file_name: None

        def _write_log(self, level: str, msg: str) -> None:
            """ Base saving method logs to file."""
            with open(self.file_name, 'a') as log_file:
                log_file.write(f'[{level}] {msg}\n')

        def critical(self, msg: str) -> None:
            self._write_log('CRITICAL', msg)

        def error(self, msg: str) -> None:
            self._write_log('ERROR', msg)

        def warn(self, msg: str) -> None:
            self._write_log('WARN', msg)

        def info(self, msg: str) -> None:
            self._write_log('INFO', msg)

        def debug(self, msg: str) -> None:
            self._write_log('DEBUG', msg)

    __instance: Optional[__Logger] = None

    def __new__(cls, *args, **kwargs):

        if not cls.instance:
            cls.__instance = cls.__Logger(*args, **kwargs)

        return Logger.__instance

    def __getattr__(self, item):
        return getattr(self.__instance, item)

    def __setattr__(self, key, value):
        return setattr(self.__instance, key, value)
