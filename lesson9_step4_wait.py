import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/explicit_wait2.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    WebDriverWait(browser,5).until(expected_conditions.text_to_be_present_in_element((By.CSS_SELECTOR, '#price'),"$100"))
    browser.find_element(By.CSS_SELECTOR, '#book').click()

    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, '.form-control').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '#solve').click()
finally:
    time.sleep(5)
    browser.quit()

