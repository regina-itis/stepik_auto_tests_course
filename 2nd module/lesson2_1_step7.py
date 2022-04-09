from selenium import webdriver
import time 
import math

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/get_attribute.html"

try:
    browser = webdriver.Chrome()
    browser.get(link)

    treasure = browser.find_element_by_id("treasure")
    x = treasure.get_attribute("valuex")
    y = calc(x)
    answer = browser.find_element_by_id("answer")
    answer.send_keys(y)
    check = browser.find_element_by_id("robotCheckbox")
    check.click()
    radio = browser.find_element_by_id("robotsRule")
    radio.click()
    button = browser.find_element_by_css_selector("button[type=\"submit\"]")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(30)
    # закрываем браузер после всех манипуляций
    browser.quit()

