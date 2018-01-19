from selene.api import browser


def test_google(app):
    app.help.open_google()


def test_yandex(app):
    app.help.open_yandex()
    assert browser.driver().current_url.endswith('yandex.ru/'), 'Current URL ends with another name'


def test_rbc(app):
    app.help.open_rbc()