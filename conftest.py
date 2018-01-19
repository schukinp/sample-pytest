import pytest

from application import Application


@pytest.fixture(scope='session')
def app():
    fixture = Application()
    yield fixture
    fixture.destroy()
