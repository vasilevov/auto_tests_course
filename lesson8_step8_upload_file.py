import time
import os
from selenium import webdriver
from selenium.webdriver.common.by import By


link = "http://suninjuly.github.io/file_input.html"
browser = webdriver.Chrome()

try:
    browser.get(link)

    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter first name"]').send_keys('Name')
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter last name"]').send_keys('Last name')
    browser.find_element(By.CSS_SELECTOR, '[placeholder="Enter email"]').send_keys('email@mail.ru')
    current_dir = os.path.abspath(os.path.dirname(__file__))
    file_path = os.path.join(current_dir, 'testfile.txt')
    browser.find_element(By.CSS_SELECTOR, '#file').send_keys(file_path)
    browser.find_element(By.CSS_SELECTOR, '.btn').click()
finally:
    time.sleep(5)
    browser.quit()

