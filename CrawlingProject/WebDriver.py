"""
selenium  환경 설정.

@author : khk37601
@date : 2020-05-02
"""
from DriverSetting import Driver
from selenium import webdriver


class BrowserDriver(Driver):

    def __init__(self, driver_path="./chromedriver", browser="chrome"):
        self.options = None
        self.__driver = None
        self.browser = browser.lower()

        if self.browser == "firefox":
            self.options = webdriver.FirefoxOptions()
        elif self.browser == "chrome":
            self.options = webdriver.ChromeOptions()
            self.options.add_argument("lang=ko_KR")
            self.options.add_argument(
                "user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) "
                "AppleWebKit/537.36 (KHTML, like Gecko)"
                "Chrome/61.0.3163.100 Safari/537.36")
        # 이외 드라이브
        else:
            raise Exception

        self.options.add_argument('--headless')
        self.options.add_argument("--disable-gpu")

        try:
            if self.browser == "firefox":
                cap = DesiredCapabilities().FIREFOX
                cap["marionette"] = True
                binary = FirefoxBinary("/usr/bin/firefox")
                self.__options.binary = binary
                self.__driver = webdriver.Firefox(firefox_options=self.__options, capabilities=cap, executable_path="./geckodriver"
            elif self.browser == "chrome":
                self.__driver = webdriver.Chrome(executable_path=driver_path,
                                                 chrome_options=self.options)
        except FileNotFoundError or FileExistsError or Exception as e:
            print(e, "드라이브 경로를 확인 해주세요")

    @property
    def get_driver(self):
        if self.browser == "chrome":
            self.__driver.execute_script(
                "Object.defineProperty(navigator, "
                "'plugins', {get: function() {return[1, 2, 3, 4, 5]}})")

            self.__driver.execute_script(
                "Object.defineProperty(navigator, 'languages',"
                " {get: function() {return ['ko-KR', 'ko']}})")

        return self.__driver
