import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
driver = webdriver.Chrome()
driver.implicitly_wait(5)
driver.maximize_window()
driver.get("http://practice.automationtesting.in/")
my_account = driver.find_element_by_partial_link_text("My Account").click()
user_name = driver.find_element_by_id("username").send_keys("marinin.alexander@supermail.com")
password = driver.find_element_by_id("password").send_keys("NebulaeAndromeda2021")
log_btn = driver.find_element_by_xpath("//*[@value = 'Login']").click()
shop = driver.find_element_by_partial_link_text("Shop").click()
cat_html = driver.find_element_by_link_text("HTML").click()

#Verficiation for the desired books on the page 

first_book = driver.find_element_by_xpath("//*[@data-product_id = '181']")
second_book = driver.find_element_by_xpath("//*[@data-product_id = '182']")
third_book = driver.find_element_by_xpath("//*[@data-product_id = '163']")
if first_book and second_book and third_book is not None:
    print("There are three books displayed on the webpage in HTML category")
else:
    print ("The number of books in HMTL category is not 3")



f_book = driver.find_element_by_xpath("//*[@title = 'Mastering HTML5 Forms']")
f_book_title = f_book.get_attribute('title')
assert f_book_title == "Mastering HTML5 Forms"
s_book = driver.find_element_by_css_selector(".products>.post-182>.woocommerce-LoopProduct-link>img")
s_book_title = s_book.get_attribute('title')
assert s_book_title == "HTML5 Web Application Development Beginner's guide"
th_book = driver.find_element_by_xpath("//*[@title = 'Thinking in HTML']")
th_book_title = th_book.get_attribute('title')
assert th_book_title == "Thinking in HTML"
print("There are three books: ",f_book_title, ', ', s_book_title,', ', th_book_title)


# Name test and picture check

book1 = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//h3[text()='HTML5 Forms']"), "HTML5 Forms"))
time.sleep(1)
book2 = WebDriverWait(driver, 10).until(EC.text_to_be_present_in_element((By.XPATH, "//h3[text()='HTML5 WebApp Develpment']"), "HTML5 WebApp Develpment"))
time.sleep(1)
book3 = WebDriverWait(driver, 10).until((EC.text_to_be_present_in_element((By.XPATH, "//h3[text()='Thinking in HTML']"), "Thinking in HTML")))
driver.quit()

