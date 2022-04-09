from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time 
import math

link = "http://suninjuly.github.io/selects2.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)
    x = browser.find_element_by_id("num1").text
    print(x)
    y = browser.find_element_by_id("num2").text
    print(y)
    z = str(int(x) + int(y))
    print(z)
    select = Select(browser.find_element_by_tag_name("select"))
    select.select_by_value(z)
    button = browser.find_element_by_css_selector("button[type=\"submit\"]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()
    