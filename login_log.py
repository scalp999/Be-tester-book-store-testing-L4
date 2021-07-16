from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
my_account_menu = driver.find_element_by_css_selector("#menu-item-50").click()
user_name = driver.find_element_by_id("username").send_keys("marinin.alexander@supermail.com")
password = driver.find_element_by_id("password").send_keys("NebulaeAndromeda2021")
log_btn = driver.find_element_by_xpath("//*[@value = 'Login']").click()
logout_btn = driver.find_element_by_link_text("Logout")
# Element text check
logout_text = logout_btn.text
assert logout_text == "Logout"
# Expected condition element presence check
logout_btn_checkEC = WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.LINK_TEXT, 'Logout')))
driver.quit()
