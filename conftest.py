import pytest

from page.SekormPage.index import IndexPage

_driver = None

@pytest.fixture()
def driver():
    global _driver
    if _driver is None:
        _driver = IndexPage()
        _driver.get_url('https://www.telerik.com/support/demos')

    return _driver

@pytest.fixture(scope='session', autouse=True)
def quit_driver():
    yield
    global _driver
    if isinstance(_driver, IndexPage):
        _driver.driver.quit()
    _driver = None
