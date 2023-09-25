import time

from selenium import webdriver
from selenium.webdriver.common.by import By


def checkboxes(check1, check2):
    driver = webdriver.Chrome()
    try:
        driver.get("https://the-internet.herokuapp.com/checkboxes")
        cb1 = driver.find_element(By.CSS_SELECTOR,
                                  "#checkboxes > input[type:checkbox]:nth-child(1)")
        cb2 = driver.find_element(By.CSS_SELECTOR,
                                  "#checkboxes > input[type:checkbox]:nth-child(3)")

        cb1_checked = cb1.get_property("checked")
        cb2_checked = cb2.get_property("checked")
        if cb1_checked and not check1:
            cb1.click()

        if not cb1_checked and check1:
            cb1.click()

        if cb2_checked and not check2:
            cb1.click()

        if not cb2_checked and check2:
            cb1.click()

    finally:
        time.sleep(3)
        driver.quit()


checkboxes(True, True)
