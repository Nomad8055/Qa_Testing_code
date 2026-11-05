import pytest
from pages.login_page import LoginPage


def test_login_page_open(page):
    login = LoginPage(page)

    login.open_login_page()

    assert page.title() != ""


def test_invalid_login(page):
    login = LoginPage(page)

    login.open_login_page()

    login.login(
        "wronguser",
        "wrongpassword"
    )

    assert page.url == "https://staging.dashboard.exportgenius.in/login"


@pytest.mark.parametrize(
    "username,password",
    [
        ("wronguser", "wrongpass"),
        ("", "password123"),
        ("username", ""),
    ]
)
def test_invalid_credentials(page, username, password):

    login = LoginPage(page)

    login.open_login_page()

    login.login(username, password)

    assert page.url == "https://staging.dashboard.exportgenius.in/login"