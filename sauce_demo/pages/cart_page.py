from playwright.sync_api import Page
from .base_page import BasePage
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sauce_demo import SauceDemo

class CartPage(BasePage):

    def __init__(self, page, sauce: "SauceDemo"):
        super().__init__(page)
        self.page = page
        self.sauce = sauce
