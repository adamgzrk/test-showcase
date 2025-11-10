from .pages import LoginPage, InventoryPage, CartPage, CheckoutPage, Users, TimeOut
from playwright.sync_api import Page


class SauceDemo:
    """"""

    def __init__(self, page: Page):
        self.page = page
        
        self.login_page = LoginPage(self.page, self)
        self.inventory_page = InventoryPage(self.page, self)
        self.cart_page = CartPage(self.page, self)
        self.checkout_page = CheckoutPage(self.page, self)
        self.users = Users
        self.timeout = TimeOut

    def skip_to_inventory_page(self, user: str = Users.STANDARD, password:str = Users.PASSWORD):
        "Open login page and log in."
        self.login_page.navigate()
        self.login_page.login(user, password)
