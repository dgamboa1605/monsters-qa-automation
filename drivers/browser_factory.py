from selenium import webdriver

class BrowserFactory:

    @staticmethod
    def get_browser(browser_name):
        if browser_name == "chrome":
            return webdriver.Chrome()
        else:
            raise ValueError("Browser not supported")
