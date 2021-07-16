import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.support.ui import Select
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get('http://practice.automationtesting.in/')
shop_menu = driver.find_element_by_link_text("Shop").click()
book_add = driver.find_element_by_xpath("//*[@data-product_id='182']").click()
time.sleep(3)
cart = driver.find_element_by_css_selector(".cartcontents").click()
proceed = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.PARTIAL_LINK_TEXT, "PROCEED TO"))).click()
first_name_EC = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "billing_first_name"))).send_keys("Alexander")
last_name = driver.find_element_by_id("billing_last_name").send_keys("Marinin")
email = driver.find_element_by_id("billing_email").send_keys("alexsupermail@gmail.com")
phone = driver.find_element_by_id("billing_phone").send_keys("1234567890")
address = driver.find_element_by_id("billing_address_1").send_keys("555 Oak avenue")
city = driver.find_element_by_id("billing_city").send_keys("Toronto")
postalcode = driver.find_element_by_id("billing_postcode").send_keys("M3Z2R7")
selector_country = driver.find_element_by_xpath("//*[@class = 'select2-container country_to_state country_select']").click()
country_choice = driver.find_element_by_id("s2id_autogen1_search").send_keys("Canada")
country_choice_click = driver.find_element_by_id("select2-results-1").click()
province_choice = WebDriverWait(driver, 10).until(EC.element_to_be_clickable((By.ID, "select2-chosen-2"))).click()
province_prompt_choice = driver.find_element_by_id("s2id_autogen2_search").send_keys("Ontario")
province_click = driver.find_element_by_css_selector(".select2-match").click()
driver.execute_script("window.scrollBy(0,600);")
time.sleep(3)
payment_check = driver.find_element_by_id("payment_method_cheque").click()
place_order = driver.find_element_by_id("place_order").click()
order_thanks_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".woocommerce-thankyou-order-received"), "Thank you. Your order has been received."))
check_payment = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "tfoot :nth-child(3) td"), "Check Payments"))
driver.quit()







