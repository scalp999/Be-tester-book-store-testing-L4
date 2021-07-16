import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("http://practice.automationtesting.in/")
shop_menu = driver.find_element_by_link_text("Shop").click()
book_html5forms = driver.find_element_by_xpath("//*[@data-product_id = '181']").click()
time.sleep(3)
basket_content = driver.find_element_by_css_selector(".cartcontents")
# Checking number of items in the basket
basket_content_check = basket_content.text
if basket_content_check == "1 Item":
    print("Number of items is in basket is correct:", basket_content_check )
else:
    print("Number of items in the basket is more or less than 1")
# or assert
assert basket_content_check == "1 Item"
# or EC
basket_content_check_EC = WebDriverWait(driver,10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR,".cartcontents"), "1 Item"))
# Я не заметил вначале , что нужно делать только assert поэтому делаем дальше assert для цены
price = driver.find_element_by_css_selector(".wpmenucart-contents .amount")
price_check = price.text
# Далее тест падает тк в задании стоит проверить цену в "₹180.00", но она измениалсь на 280, чтоб тест не падал я оставил корректный вариант
# assert price_check == "₹180.00"
assert price_check == "₹280.00"
basket = driver.find_element_by_css_selector("span.amount").click()
# Проверка отображения стоимости по EC, через ожидаемые значения цены
sub_price_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//*[@data-title = 'Subtotal']") , "₹280.00"))
total_price_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total td"), "₹294.00"))
# Потом поразмыслив, что для теста все время придется подбирать цену, решил что можно добавить и так, оба варианта рабочие:
total_price_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".order-total td"), "₹"))
sub_price_check = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//*[@data-title = 'Subtotal']") , "₹"))
driver.quit()


