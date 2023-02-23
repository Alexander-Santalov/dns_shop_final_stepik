import re

from selenium.webdriver.common.by import By


class CartPageHelper:

    def __init__(self, app):
        self.app = app

    text_product_in_cart = (By.CSS_SELECTOR, 'div.cart-items__product-name')
    price_product_in_cart = (By.CSS_SELECTOR, '.cart-tab-products-list span.price__current')
    price_summary = (By.CSS_SELECTOR, '.cart-tab-total-amount span.price__current')
    equal_product_total = (By.CSS_SELECTOR, 'div.summary-header__total-items')
    equal_product_in_cart = (By.CSS_SELECTOR, 'input.count-buttons__input')

    def assert_result_in_cart(self):
        self.app.methods.click(*self.app.filter_page.btn_cart)
        text_tv_in_cart = self.app.methods.get_text(*self.text_product_in_cart)
        assert self.app.filter_page.text_tv == text_tv_in_cart, \
            f'\nОжидаемый результат  : {self.app.filter_page.text_tv}\nФактический результат: {text_tv_in_cart}'
        price_tv_in_cart = self.app.methods.get_text(*self.price_product_in_cart)
        price_tv_in_cart = int(''.join(re.findall(r'\d+', price_tv_in_cart)))
        assert self.app.filter_page.price_tv == price_tv_in_cart,\
            f'\nОжидаемый результат  : {self.app.filter_page.price_tv}\nФактический результат: {price_tv_in_cart}'
        self.app.methods.assert_element_param(*self.equal_product_in_cart, 'value', '1')
        price_tv_summary = self.app.methods.get_text(*self.price_summary)
        price_tv_summary = int(''.join(re.findall(r'\d+', price_tv_summary)))
        assert self.app.filter_page.price_tv == price_tv_summary, \
            f'\nОжидаемый результат  : {self.app.filter_page.price_tv}\nФактический результат: {price_tv_summary}'
        self.app.methods.assert_element_text(*self.equal_product_total, '1 товар')

