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
shop_btn = driver.find_element_by_link_text("Shop").click()
html_books = driver.find_element_by_link_text("HTML").click()
html5_book = driver.find_element_by_partial_link_text("HTML5 Forms").click()
header = driver.find_element_by_xpath("//*[@class = 'product_title entry-title']")
# Text check for book title "HTML5 Forms"
header_text = header.text
assert header_text == "HTML5 Forms"
# or
header_text_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//*[@class = 'product_title entry-title']"), "HTML5 Forms"))
driver.quit()