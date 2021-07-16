import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
my_account_menu = driver.find_element_by_css_selector("#menu-item-50").click()
email = driver.find_element_by_id("reg_email").send_keys("marinin.alexander@supermail.com")
password = driver.find_element_by_id("reg_password").send_keys("NebulaeAndromeda2021")
register_btn = driver.find_element_by_xpath("//*[@value = 'Register']")
time.sleep(1)
register_btn.click()
driver.quit()


