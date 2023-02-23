from selenium.webdriver.common.by import By


class MainPageHelper:

    def __init__(self, app):
        self.app = app

    field_search = (By.CSS_SELECTOR, "[placeholder='Поиск по сайту']")
    btn_search = (By.CSS_SELECTOR, '.presearch__icon-search')
    text_contact = (By.CSS_SELECTOR, '.menu-contacts__title')

    def open_home_page(self):
        wd = self.app.wd
        wd.get("https://www.dns-shop.ru/")
        self.app.methods.wait_to_be_text(*self.text_contact, 'Оставайтесь на связи')
        print

    def choose_tv_by_search(self):
        self.app.methods.type_value(*self.field_search, 'Телевизоры')
        self.app.methods.click(*self.btn_search)
