import time
from selenium import webdriver
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/ ")
shop_menu = driver.find_element_by_link_text("Shop").click()
driver.execute_script("window.scrollBy(0,300);")
book1_add = driver.find_element_by_xpath("//*[@data-product_id = '182']").click()
time.sleep(5)
book2_add = driver.find_element_by_xpath("//*[@data-product_id = '180']").click()
shopping_cart = driver.find_element_by_css_selector(".cartcontents").click()
time.sleep(5)
remove_1 = driver.find_element_by_xpath("//*[@data-product_id='182']").click()
time.sleep(5)
undo = driver.find_element_by_partial_link_text("Undo?").click()
quantity = driver.find_element_by_xpath("//*[@name = 'cart[045117b0e0a11a242b9765e79cbf113f][qty]']")
quantity.clear()
quantity.send_keys('3')
update_btn = driver.find_element_by_xpath(" //*[@value = 'Update Basket']").click()
quantity_number_check = quantity.get_attribute('value')
assert quantity_number_check == '3'
time.sleep(3)
coupon = driver.find_element_by_xpath(" //*[@value = 'Apply Coupon']").click()
text_coupon = driver.find_element_by_css_selector(".woocommerce-error li")
text_coupon_check = text_coupon.text
assert text_coupon_check == "Please enter a coupon code."
driver.quit()






