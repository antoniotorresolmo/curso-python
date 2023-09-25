import selenium
from selenium.webdriver.common.by import By


class PortalPage(object):
    def __init__(self, driver):
        self.driver = driver
        # Elementos
        self.txt_username = lambda: self.driver.find_element(By.ID, "username")
        self.txt_password = lambda: self.driver.find_element(By.ID, "password")
        self.btn_login = lambda: self.driver.find_element(By.CSS_SELECTOR, "#login > button")

    def get(self):
        self.driver.get("https://the-internet.herokuapp.com/login")
        return self