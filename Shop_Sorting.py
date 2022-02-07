from selenium import webdriver
from selenium.webdriver.support.select import Select
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
selector = driver.find_element_by_css_selector("select.orderby")
value_selector_check = selector.get_attribute('value')
# First option to check the status of selector
if value_selector_check == "menu_order":
    print("Default order is selected")
else:
    print("Other order was selected")
# Second option to check the selector
assert value_selector_check == "menu_order"

# or
sort_order_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "select.orderby"), 'Default'))

selector = driver.find_element_by_css_selector("select.orderby")
select = Select(selector)
select.select_by_value('price-desc')
selector = driver.find_element_by_css_selector("select.orderby")

# Lets do both checks again

value_selector_check = selector.get_attribute("value")
if value_selector_check == "price-desc":
    print ("Ascending sorting was chosen")
else:
    print("Other sorting method was chosen")
# or

assert value_selector_check == 'price-desc'

#or

sort_order_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "select.orderby"), 'high to low'))
driver.quit()








