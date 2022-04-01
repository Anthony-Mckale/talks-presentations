from abc import ABC, abstractmethod


class BaseClassMeta(ABC):
    @staticmethod
    @abstractmethod
    def do_some_static_thing(value: str) -> str:
        """some doc"""

    @abstractmethod
    def do_some_thing(self, value: str) -> str:
        """some doc"""


class BarClass(BaseClassMeta):
    def __init__(self):
        # do something
        self.value = "bar"

    @staticmethod
    def do_some_static_thing(value: str) -> str:
        return "bar" + value

    def do_some_thing(self, value: str) -> str:
        """some doc"""
        return self.value + value


class FooClass(BaseClassMeta):
    def __init__(self):
        # do something
        self.value = "foo"

    @staticmethod
    def do_some_static_thing(value: str) -> str:
        return "foo" + value

    def do_some_thing(self, value: str) -> str:
        """some doc"""
        return "sdfsdfsdfsdf" + value


bar = BarClass()
foo = FooClass()
print(bar.do_some_thing('ting'))
print(foo.do_some_thing('ting'))

# print("Can not create ABC directly")
# abstract = BaseClassMeta()
# abstract.do_some_thing('ting')
