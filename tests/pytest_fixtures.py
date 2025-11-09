import pytest
from pytest import FixtureRequest
from playwright.sync_api import sync_playwright, Playwright, Browser, BrowserContext, Page


@pytest.fixture(scope="session")
def playwright_inst():
    with sync_playwright() as p:
        yield p

@pytest.fixture(scope="session")
def browser_chrome(playwright_inst: Playwright):
    browser = playwright_inst.chromium.launch(headless=False)
    yield browser
    browser.close()

@pytest.fixture
def context_chrome(browser_chrome: Browser):
    context = browser_chrome.new_context()
    yield context
    context.close()

@pytest.fixture
def page_chrome(request: FixtureRequest, browser_chrome: Browser, context_chrome: BrowserContext):
    if request.param == "desktop":
        page = context_chrome.new_page()
    elif request.param == "mobile":
        context = browser_chrome.new_context(
            user_agent="Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/103.0.5060.63 Mobile/15E148 Safari/604.1",
            viewport={"width": 390, "height": 844}
        )
        page = context.new_page()
    yield page
    page.close()
