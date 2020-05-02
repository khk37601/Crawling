"""
@author : khk37601
@date : 2020-05-02
"""
from abc import *
from WebDriver import BrowserDriver


class CrawlingSetting(metaclass=ABCMeta):

    def __init__(self, driver_path, driver_type=None):
        if driver_type is None:
            exit(-1)
        else:
            BrowserDriver(driver_path, driver_type).get_driver()

    def run_crawling(self, start, end, driver):
        pass
