import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/alert_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    browser.switch_to.alert.accept()
    WebDriverWait(browser,5).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, "#input_value")))
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, '.form-control').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
finally:
    time.sleep(5)
    browser.quit()

