from pages.main_page import MainPageHelper
from pages.filter_page import FilterPageHelper
from pages.cart_page import CartPageHelper
from .methods import MethodHelper


class Application:

    def __init__(self, browser):
        self.wd = browser
        self.main_page = MainPageHelper(self)
        self.filter_page = FilterPageHelper(self)
        self.cart_page = CartPageHelper(self)
        self.methods = MethodHelper(self)
        self.wd.set_window_size(1920, 1080)

