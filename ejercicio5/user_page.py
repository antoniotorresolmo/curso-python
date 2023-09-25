import selenium
from selenium.webdriver.common.by import By


class UserPage(object):
    def __init__(self, driver):
        self.driver = driver
        # Elementos
        self.btn_logout = lambda: self.driver.find_element(By.CSS_SELECTOR, ".button")
