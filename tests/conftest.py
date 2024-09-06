import pytest

from drivers.browser_factory import BrowserFactory
from config import config

@pytest.fixture
def browser():
    browser = BrowserFactory.get_browser(config.BROWSER)
    browser.get(config.URL)
    yield browser
    browser.quit()
