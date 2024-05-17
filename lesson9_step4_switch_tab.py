import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = "http://suninjuly.github.io/redirect_accept.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
    windows = browser.window_handles
    browser.switch_to.window(windows[1])
    x = browser.find_element(By.CSS_SELECTOR, "#input_value").text
    y = calc(x)
    browser.find_element(By.CSS_SELECTOR, '.form-control').send_keys(y)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
finally:
    time.sleep(5)
    browser.quit()

