from .base_page import BasePage
from playwright.sync_api import Page


class LoginPage(BasePage):

    URL = "https://www.saucedemo.com/"
    USERNAME_FIELD = "#user-name.input_error.form_input"
    PASSWORD_FIELD = "#password.input_error.form_input"
    LOGIN_BTN = "#login-button.submit-button.btn_action"
    ERR_DTID = "error"

    def __init__(self, page: Page):
        self.page = page
        super().__init__(self.page)


    def navigate(self, wait_until: str = "load", timeout: int = 10_000):
        """
        Navigate to saucedemo login page.
        
        Args:
            wait_until (str): wait for state, e. g. "load", "networkidle", "domcontentlodaded"
            timeout (int): timeout in milliseconds
        """
        self._navigate(self.URL, wait_until, timeout)

    def login(self, user: str, password: str):
        """
        Login as given user.

        Args:
            user (str): User UID
            password (str): Password
        """
        self.fill(self.USERNAME_FIELD, user)
        self.fill(self.PASSWORD_FIELD, password)
        self._click(self.LOGIN_BTN)
    
    def get_error_container_text(self):
        "Return text from error msg container."
        return self.page.get_by_test_id(self.ERR_DTID).text_content()
        