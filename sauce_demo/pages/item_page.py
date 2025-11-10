from playwright.sync_api import Page
from .base_page import BasePage
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sauce_demo import SauceDemo

class ItemPage(BasePage):
    ""
    
    ADD_BTN_PREFIX = "#add-to-cart"
    REMOVE_BTN_PREFIX = "#remove"
    BTN_POSTFIX = ".btn.btn_secondary.btn_small.btn_inventory"

    ITEM_NAME = '[data-test="inventory-item-name"]'
    PRICE = '[data-test="inventory-item-price"]'

    BACK_TO_PROD_BTN = '[data-test="back-to-products"]'


    def __init__(self, page: Page, sauce: "SauceDemo"):
        super().__init__(page)
        self.page = page
        self.sauce = sauce

    def click_button(self, action: str = "add"):
        """
        Click on add/remove button. Define action by passing "add" or "remove" as action param.
        """
        if action == "remove":
            selector = self.REMOVE_BTN_PREFIX
        else:
            selector = self.ADD_BTN_PREFIX
        self.page.click(selector + self.BTN_POSTFIX)

    def get_item_name(self):
        "Return item name"
        self._get_text(self.ITEM_NAME)

    def get_item_price(self, make_float: bool = False):
        "Return item price"
        if not make_float:
            return self._get_text(self.PRICE)
        else:
            return float(self._get_text(self.PRICE).strip("$"))

    def click_back_to_products(self):
        "Click on Back to products button"
        self.page.click(self.BACK_TO_PROD_BTN)

