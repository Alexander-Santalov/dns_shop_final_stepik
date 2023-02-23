from selenium.common import TimeoutException
from selenium.webdriver import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MethodHelper:

    def __init__(self, app):
        self.app = app

    def click(self, locator_strategies, locator):
        try:
            wd = self.app.wd
            WebDriverWait(wd, 10).until(EC.element_to_be_clickable((locator_strategies, locator))).click()
        except Exception as e:
            assert e == TimeoutException, f"Ошибка! Нет возможности кликнуть по локатору: '{locator}'"

    def type_value(self, locator_strategies, locator, value):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(EC.element_to_be_clickable((locator_strategies, locator)))
            element.clear()
            element.send_keys(value)
        except Exception as e:
            assert e == TimeoutException, f"Ошибка локатор поля ввода '{locator}' - не найден"

    def wait_to_be_text(self, locator_strategies, locator, text):
        wd = self.app.wd
        try:
            WebDriverWait(wd, 10).until(EC.text_to_be_present_in_element((locator_strategies, locator), text))
        except Exception as e:
            assert e == TimeoutException, f"Искомый текст '{text}' не отобразился"

    def scroll_to_element(self, locator_strategies, locator):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(EC.presence_of_element_located((locator_strategies, locator)))
            ActionChains(wd).scroll_to_element(element).perform()
        except Exception as e:
            assert e == TimeoutException, f"Ошибка, локатор {locator} - не найден"

    def check_hide_element(self, locator_strategies, locator, locator_strategies_action, locator_action):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 10).until(
                EC.visibility_of_element_located((locator_strategies, locator)))
            self.click(locator_strategies_action, locator_action)
            WebDriverWait(wd, 10).until(EC.staleness_of(element))
        except Exception as e:
            assert e == TimeoutException, f"Элемент продолжает отображаться"

    def get_text(self, locator_strategies, locator):
        wd = self.app.wd
        return WebDriverWait(wd, 5).until(EC.presence_of_element_located((locator_strategies, locator))).text

    def assert_element_param(self, locator_strategies, locator, param, expected_value):
        try:
            wd = self.app.wd
            field_value = WebDriverWait(wd, 5).until(
                EC.presence_of_element_located((locator_strategies, locator)))
            actual_value = field_value.get_attribute(param)
            assert actual_value == expected_value, \
                f"\nОжидаемый результат = {expected_value},\nФактический = {actual_value}"
        except Exception as e:
            assert e == TimeoutException, f"Ошибка, локатор {locator} - не найден"

    def assert_element_text(self, locator_strategies, locator, text):
        try:
            wd = self.app.wd
            element = WebDriverWait(wd, 5).until(
                EC.visibility_of_element_located((locator_strategies, locator)))
            assert element.text == text, f"\nОжидаемый результат = {text},\nФактический = {element.text}"
        except Exception as e:
            assert e == TimeoutException, f"Ошибка, локатор {locator} - не найден"
