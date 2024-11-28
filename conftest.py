import pytest

from page.SekormPage.index import IndexPage

@pytest.fixture()
def driver():
    a = IndexPage()
    return a