
import pytest
from playwright.sync_api import sync_playwright


@pytest.fixture
def page():
    with sync_playwright() as p:

        browser = p.chromium.launch(
            headless=True
        )

        context = browser.new_context(
            ignore_https_errors=True
        )

        page = context.new_page()

        yield page

        context.close()
        browser.close()
