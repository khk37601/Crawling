# sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))
from WebDriver import BrowserDriver


if __name__ == "__main__":
    driver = BrowserDriver("C:/Users/khk37/Desktop/Crawlings/chromedriver").get_driver
    driver.get("https://www.google.com")
    print(driver.page_source)
    driver.quit()
