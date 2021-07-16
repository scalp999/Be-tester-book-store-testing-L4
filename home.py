from selenium import webdriver
driver = webdriver.Chrome()
driver.maximize_window()
driver.get('http://practice.automationtesting.in/')
driver.implicitly_wait(5)
driver.execute_script("window.scrollBy(0, 600);")
sel_ruby_book = driver.find_element_by_xpath("//*[contains(text(), 'Selenium Ruby')]").click()
ruby_reviews = driver.find_element_by_partial_link_text("REVIEWS").click()
star_review = driver.find_element_by_css_selector(".star-5").click()
review_text = driver.find_element_by_css_selector("#comment")
review_text.send_keys("Nice Book!")
name = driver.find_element_by_css_selector("input#author").send_keys("Alexander Marinin")
email = driver.find_element_by_css_selector("input#email").send_keys("marinin.alexander@supermail.com")
sumbit_btn = driver.find_element_by_id("submit").click()
driver.quit()


