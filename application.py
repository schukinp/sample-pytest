from selene import browser
from selenium import webdriver

from helpers import UrlHelper


class Application:

    def __init__(self):
        browser.set_driver(webdriver.Chrome())
        self.help = UrlHelper(self)

    def destroy(self):
        browser.driver().quit()


