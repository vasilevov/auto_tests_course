import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

def calc(x, y):
  return int(x) + int(y)

link = "http://suninjuly.github.io/selects1.html"
browser = webdriver.Chrome()

try:
    browser.get(link)
    x = browser.find_element(By.CSS_SELECTOR, "#num1").text
    y = browser.find_element(By.CSS_SELECTOR, "#num2").text
    sum = str(calc(x, y))
    list = Select(browser.find_element(By.CSS_SELECTOR, '#dropdown'))
    list.select_by_value(sum)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
finally:
    time.sleep(5)
    browser.quit()

