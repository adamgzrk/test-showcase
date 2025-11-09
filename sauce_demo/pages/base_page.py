from enum import IntEnum, StrEnum
from playwright.sync_api import Page


class TimeOut(IntEnum):
    SHORT = 3_000
    DEFAULT = 10_000
    LONG = 30_000
    LONGEST = 60_000


class Users(StrEnum):
    STANDARD = "standard_user"
    LOCKED_OUT = "locked_out_user"
    PROBLEM = "problem_user"
    PERFORMANCE_GLITCH = "performance_glitch_user"
    ERROR = "error_user"
    VISUAL = "visual_user"
    PASSWORD = "secret_sauce"


class LoadStates(StrEnum):
    pass


class BasePage:

    def __init__(self, page: Page):
        """
        Initializes BasePage instance
        
        Args:
        page (Page): A Playwright page instance.
        """
        self.page = page
        self.timeout = TimeOut


    def _navigate(self, url: str, wait_until: str, timeout: int):
        "Goto given url."
        self.page.goto(url, wait_until=wait_until, timeout=timeout)
    
    def _click(self, locator: str):
        "Click on given locator."
        self.page.click(locator)

    def _get_text(self, selector: str) -> str:
        "Return text of given selector."
        return self.page.text_content(selector)
        
    def _is_visible(self, selector: str) -> bool:
        "Return bool value if given selector is visible."
        return self.page.is_visible(selector)

    def fill(self, selector: str, text: str):
        "Fill given selector (if possible) with provided text."        
        self.page.fill(selector, value=text)
