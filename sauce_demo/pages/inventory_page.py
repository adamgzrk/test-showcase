from playwright.sync_api import Page
from .base_page import BasePage
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from sauce_demo import SauceDemo


class InventoryPage(BasePage):
    
    URL = "https://www.saucedemo.com/inventory.html"

    # MENU RELATED SELECTORS
    BURG_MENU = "#react-burger-menu-btn"
    MENU_ALL_ITEMS = '[data-test="inventory-sidebar-link"]'
    MENU_ABOUT = '[data-test="about-sidebar-link"]'
    MENU_LOGOUT = '[data-test="logout-sidebar-link"]'
    MENU_RESET_APP = '[data-test="reset-sidebar-link"]'
    ADD_ITEM_PREFIX = "add-to-cart-"

    items_dict = {
        "backpack": "sauce-labs-backpack",
        "bike_light": "sauce-labs-bike-light",
        "bolt_tshirt": "sauce-labs-bolt-t-shirt",
        "jacket": "sauce-labs-fleece-jacket",
        "onesie": "sauce-labs-onesie",
        "red_tshirt": "test.allthethings()-t-shirt-(red)",
        }

    def __init__(self, page: Page, sauce: "SauceDemo"):
        super().__init__(page)
        self.page = page
        self.sauce = sauce


    def navigate(self):
        "Navigate to inventory page"
        self._navigate(self.URL)

    def open_burger_menu(self):
        "Click on burger menu"
        self.page.click(self.BURG_MENU)

    def burger_menu_select(self, section: str):
        """
        Click on given section in burger menu. Available choices are: "all_items", "about", "logout", "reset_app".
        """
        if section == "all_items":
            self.page.click(self.MENU_ALL_ITEMS)
        elif section == "about":
            self.page.click(self.MENU_ABOUT)
        elif section == "logout":
            self.page.click(self.MENU_LOGOUT)
        elif section == "reset_app":
            self.page.click(self.bm_select_reset_app)

    def add_item_to_cart(self, items: list = None, all: bool = False):
        """
        Add item to shopping cart.
        
        Args:
            items (list): Names of the items. Available choices are "backpack", "bike_light", "bolt_tshirt", "jacket", "onesie", "red_tshirt"
        """
        if all:
            for name, selector in self.items_dict.items():
                self.page.click(f'[data-test="{self.ADD_ITEM_PREFIX + selector}"]')
                return
        for item in items:
            self.page.click(f'[data-test="{self.ADD_ITEM_PREFIX + self.items_dict[item]}"]')
        