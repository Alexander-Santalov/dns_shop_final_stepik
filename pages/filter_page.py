import re
from selenium.webdriver.common.by import By


class FilterPageHelper:

    def __init__(self, app):
        self.app = app

    field_price_from = (By.CSS_SELECTOR, '.products-page .ui-input-small:first-child [type="number"]')
    field_price_to = (By.CSS_SELECTOR, '.products-page .ui-input-small:nth-child(2) [type="number"]')
    checkbox_samsung = (By.XPATH, '(//input[@value="samsung"]/..)[1]')
    block_maker = (By.XPATH, '//div[@data-id="brand"]')
    filter_size = (By.CSS_SELECTOR, '[data-id="fr[p2]"]')
    filter_size_55_65 = (By.XPATH, '//input[@data-min="55"]/..')
    filter_wi_fi = (By.CSS_SELECTOR, '[data-id="f[4jj]"]')
    filter_wi_fi_yes = (By.CSS_SELECTOR, '[data-id="f[4jj]"] label:first-child')
    filter_os = (By.CSS_SELECTOR, '[data-id="f[rch]"]')
    filter_os_tizen = (By.CSS_SELECTOR, '[data-id="f[rch]"] input[value="e42g"] +span')
    filter_display = (By.CSS_SELECTOR, '[data-id="f[jeso]"]')
    filter_display_qled = (By.CSS_SELECTOR, '[data-id="f[jeso]"] input[value="luzp2"] +span')
    btn_apply_filter = (By.XPATH, '//button[.="Применить"]')
    element_of_product = (By.CSS_SELECTOR, '[data-id="product"] > a')
    btn_buy = (By.CSS_SELECTOR, '[data-id="product"]:first-child button.buy-btn')
    text_product_cart_modal = (By.CSS_SELECTOR, 'div.cart-product__name')
    price_product_cart_modal = (By.CSS_SELECTOR, 'div.cart-product__price')
    btn_cart = (By.CSS_SELECTOR, 'div.cart-button')
    text_summary = (By.CSS_SELECTOR, 'div.cart-summary__price span')
    badge = (By.CSS_SELECTOR, '.cart-link-counter__badge')
    price_under_cart = (By.CSS_SELECTOR, '.cart-link-counter__price')
    title_cart_modal = (By.CSS_SELECTOR, '.cart-group__header-title')
    total_price_cart_modal = (By.CSS_SELECTOR, '.cart-summary__value')
    list_result_filter = []
    text_tv = ''
    price_tv = ''

    def set_and_apply_filters(self):
        self.app.methods.scroll_to_element(*self.field_price_from)
        self.app.methods.type_value(*self.field_price_from, '105000')
        self.app.methods.type_value(*self.field_price_to, '110000')
        self.app.methods.scroll_to_element(*self.block_maker)
        self.app.methods.scroll_to_element(*self.checkbox_samsung)
        self.app.methods.click(*self.checkbox_samsung)
        self.open_and_set_filter(self.filter_size, self.filter_size_55_65)
        self.open_and_set_filter(self.filter_wi_fi, self.filter_wi_fi_yes)
        self.open_and_set_filter(self.filter_os, self.filter_os_tizen)
        self.app.methods.scroll_to_element(*self.btn_apply_filter)
        self.app.methods.click(*self.btn_apply_filter)
        self.app.methods.check_hide_element(*self.element_of_product, *self.btn_apply_filter)

    def open_and_set_filter(self, title_locator, value_locator):
        self.app.methods.scroll_to_element(*title_locator)
        self.app.methods.click(*title_locator)
        self.app.methods.click(*value_locator)

    def assert_result_filters(self):
        wd = self.app.wd
        for element in wd.find_elements(By.CSS_SELECTOR, '[data-id="product"]'):
            price = element.find_element(By.CSS_SELECTOR, ' .product-buy__price').text
            price = int(''.join(re.findall(r'\d+', price)))
            isprice = 105000 <= price <= 110000
            assert isprice, f'Неверной значение цены {price}'
            text_tv = element.find_element(By.CSS_SELECTOR, ' a>span').text
            for value in ['Wi-Fi', 'QLED', 'Samsung', 'Tizen']:
                assert value in text_tv, f'Фильтр {value} отсутсвует в описании телевизора'
            size = int(text_tv[0:2])
            issize = 55 <= size <= 64.9
            assert issize, f'Неверной значение диаганали телевизора{issize}'
            self.list_result_filter.append(text_tv)
            self.list_result_filter.append(price)

    def assert_product_in_cart_modal(self):
        self.app.methods.scroll_to_element(*self.btn_buy)
        self.app.methods.click(*self.btn_buy)
        self.app.methods.wait_to_be_text(*self.text_summary, 'Итого:')
        self.text_tv = self.list_result_filter[0].split(' [')[0]
        text_tv_in_cart_modal = self.app.methods.get_text(*self.text_product_cart_modal)
        assert self.text_tv == text_tv_in_cart_modal, f'\nОжидаемый результат  : {self.text_tv}' \
                                                      f'\nФактический результат: {text_tv_in_cart_modal}'
        self.price_tv = self.list_result_filter[1]
        price_tv_in_cart_modal = self.app.methods.get_text(*self.price_product_cart_modal)
        price_tv_in_cart_modal = int(''.join(re.findall(r'\d+', price_tv_in_cart_modal)))
        assert self.price_tv == price_tv_in_cart_modal, f'\nОжидаемый результат  : {self.price_tv}' \
                                                        f'\nФактический результат: {price_tv_in_cart_modal}'
        self.app.methods.assert_element_text(*self.title_cart_modal, 'Основные товары (1)')

        total_cart_modal = self.app.methods.get_text(*self.total_price_cart_modal)
        total_cart_modal = int(''.join(re.findall(r'\d+', total_cart_modal)))
        assert self.price_tv == total_cart_modal, f'\nОжидаемый результат  : {self.price_tv}' \
                                                  f'\nФактический результат: {total_cart_modal}'

    def assert_display_cart(self):
        self.app.methods.assert_element_text(*self.badge, '1')
        price_tv_under_cart = self.app.methods.get_text(*self.price_under_cart)
        price_tv_under_cart = int(''.join(re.findall(r'\d+', price_tv_under_cart)))
        assert self.price_tv == price_tv_under_cart, f'\nОжидаемый результат  : {self.price_tv}' \
                                                     f'\nФактический результат: {price_tv_under_cart}'
