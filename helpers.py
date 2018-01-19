from selene.api import browser


class UrlHelper:

    def __init__(self, app):
        self.app = app

    def open_google(self):
        browser.open_url("http://www.google.ru")

    def open_yandex(self):
        browser.open_url("http://www.yandex.ru")

    def open_rbc(self):
        browser.open_url("http://www.rbc.ru")




