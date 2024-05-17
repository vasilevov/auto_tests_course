import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/execute_script.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    button = browser.find_element(By.CSS_SELECTOR, '.btn')
    browser.find_element(By.CSS_SELECTOR, '.form-control').send_keys(y)
    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    browser.find_element(By.CSS_SELECTOR, '#robotCheckbox').click()
    browser.find_element(By.CSS_SELECTOR, '#robotsRule').click()
    button.click()
finally:
    time.sleep(5)
    browser.quit()

