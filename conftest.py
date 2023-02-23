import os
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
import resourse
from base.application import Application


@pytest.fixture
def app():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    g = Service(os.path.abspath(os.path.join(os.path.dirname(resourse.__file__), 'chromedriver.exe')))
    wd = webdriver.Chrome(options=options, service=g)
    fixture = Application(wd)
    yield fixture
    wd.quit()
