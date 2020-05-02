"""
WebDriver 부모클래스.
@author : khk37601
@date : 2020-05-02
"""
from abc import *


class Driver(metaclass=ABCMeta):

    @abstractmethod
    def get_driver(self):
        pass
