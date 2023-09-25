import time

from selenium import webdriver

from ejercicio5.portal_page import PortalPage
from ejercicio5.user_page import UserPage

driver = webdriver.Chrome()

try:
    login_page = PortalPage(driver)
    login_page.get()
    login_page.txt_username().send_keys("tomsmith")
    login_page.txt_password().send_keys("SuperSecretPassword!")
    login_page.btn_login().click()

    user_page = UserPage(driver)
    is_visible = user_page.btn_logout().is_displayed()

finally:
    time.sleep(3)
    driver.quit()
