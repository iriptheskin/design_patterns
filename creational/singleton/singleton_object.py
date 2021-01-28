from dataclasses import dataclass
from typing import Optional


@dataclass
class SingletonObject:
    """ Base implementation of Singleton Object."""
    @dataclass
    class __SingletonObject:
        val: Optional = None

        # The rest of the class definition will follow here.

    __instance: Optional[__SingletonObject] = None

    def __new__(cls, *args, **kwargs):
        if not cls.__instance:
            cls.__instance = cls.__SingletonObject()

        return cls.__instance

    def __getattr__(self, item):
        return getattr(self.__instance, item)

    def __setattr__(self, key, value):
        return setattr(self.__instance, key, value)
