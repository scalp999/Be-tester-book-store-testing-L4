from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
my_account = driver.find_element_by_partial_link_text("My Account").click()
user_name = driver.find_element_by_id("username").send_keys("marinin.alexander@supermail.com")
password = driver.find_element_by_id("password").send_keys("NebulaeAndromeda2021")
log_btn = driver.find_element_by_xpath("//*[@value = 'Login']").click()
shop = driver.find_element_by_partial_link_text("Shop").click()
android_book = driver.find_element_by_partial_link_text("Android Quick Start Guide").click()
old_price = driver.find_element_by_css_selector(".price>del")
old_price_text = old_price.text
print("Old price is: ", old_price_text)
assert old_price_text == "₹600.00"
new_price = driver.find_element_by_css_selector(".price>ins")
new_price_text = new_price.text
print("New price is: ", new_price_text)
assert new_price_text == "₹450.00"
image_click = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.XPATH, "//*[@alt = 'Android Quick Start Guide']"))).click()
image_close = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.CSS_SELECTOR, ".pp_close"))).click()
driver.quit()






