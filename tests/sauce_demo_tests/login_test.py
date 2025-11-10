import pytest
from sauce_demo.sauce_demo import SauceDemo, Users
from playwright.sync_api import Page, expect


INV_USER = "invalid"
INV_PASS = "login"
AUTH_REQ_URL = "https://submit.backtrace.io/UNIVERSE/TOKEN/json"
users = [user for user in Users if "sauce" not in user] 


@pytest.mark.parametrize("user", users)
@pytest.mark.parametrize("page_chrome", ["desktop", "mobile"], indirect=True)
def test_successful_login(page_chrome: Page, user):
    sauce = SauceDemo(page_chrome)
    sauce.login_page.navigate(
        wait_until="load",
        timeout=sauce.timeout.DEFAULT
    )
    sauce.login_page.login(
        user=user, 
        password=sauce.users.PASSWORD
    )
    assert sauce.page.url == sauce.inventory_page.URL, f"Unsuccessful redirect. Page url is {sauce.page.url}, it's {sauce.page.url}"


@pytest.mark.parametrize("page_chrome", ["desktop", "mobile"], indirect=True)
def test_invalid_credentials(page_chrome: Page):
    sauce = SauceDemo(page_chrome)
    sauce.login_page.navigate()
    sauce.login_page.login(
        user=INV_USER,
        password=INV_PASS,
    )
    err_msg = sauce.login_page.get_error_container_text()
    print(err_msg)
    assert sauce.login_page.errors.WRONG_CREDENTIALS in err_msg , f"Displayed error text does not contain proper message.\nMessage: {err_msg}"


@pytest.mark.parametrize("page_chrome", ["desktop", "mobile"], indirect=True)
def test_missing_username(page_chrome: Page):
    sauce = SauceDemo(page_chrome)
    sauce.login_page.navigate()
    sauce.login_page.login(
        "",
        sauce.users.PASSWORD,
    )
    err_msg = sauce.login_page.get_error_container_text()
    assert sauce.login_page.errors.NO_LOGIN in err_msg, f"Displayed error text does not contain proper message.\nMessage: {err_msg}"


@pytest.mark.parametrize("page_chrome", ["desktop", "mobile"], indirect=True)
def test_missing_password(page_chrome: Page):
    sauce = SauceDemo(page_chrome)
    sauce.login_page.navigate()
    sauce.login_page.login(
        sauce.users.STANDARD,
        "",
    )
    err_msg = sauce.login_page.get_error_container_text()
    assert sauce.login_page.errors.NO_PASSWORD in err_msg, f"Displayed error text does not contain proper message.\nMessage: {err_msg}"


@pytest.mark.parametrize("page_chrome", ["desktop", "mobile"], indirect=True)
def test_login_and_logout(page_chrome: Page):
    sauce = SauceDemo(page_chrome)
    sauce.login_page.navigate()
    sauce.login_page.login(
        sauce.users.STANDARD,
        sauce.users.PASSWORD
    )
    sauce.inventory_page.open_burger_menu()
    sauce.inventory_page.burger_menu_select("logout")
    assert sauce.page.url == sauce.login_page.URL, f"Unsuccessful logout, page url is {sauce.page.url}"
    