from selenium import webdriver
import pytest
import main
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

link = "https://stepik.org/lesson/236895/step/1"

@pytest.mark.parametrize('lesson_id', ['236895','236896','236897','236898','236899','236903','236904','236905'])
def test_log_in(browser, lesson_id):
    link = f"https://stepik.org/lesson/{lesson_id}/step/1"
    browser.get(link)
    WebDriverWait(browser, 20).until(
        expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '#ember459')))
    browser.find_element(By.CSS_SELECTOR, '#ember459').click()
    WebDriverWait(browser,20).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,'#id_login_email')))
    browser.find_element(By.CSS_SELECTOR,'#id_login_email').send_keys(main.my_email)
    browser.find_element(By.CSS_SELECTOR,'#id_login_password').send_keys(main.my_password)
    browser.find_element(By.CSS_SELECTOR,'.sign-form__btn').click()

    WebDriverWait(browser,20).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,'.ember-text-area')))
    try:
        WebDriverWait(browser, 20).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.again-btn')))
        again_button = browser.find_element(By.CSS_SELECTOR, '.again-btn')
        if "Начать сначала" in again_button.text:
            browser.find_element(By.CSS_SELECTOR, '.ember-text-area').clear()
        else:
            again_button.click()
            WebDriverWait(browser, 20).until(
                expected_conditions.visibility_of_element_located((By.CSS_SELECTOR, '.ember-text-area')))
    except Exception:
        pass
    answer = math.log(int(time.time()))
    browser.find_element(By.CSS_SELECTOR, '.ember-text-area').send_keys(answer)
    WebDriverWait(browser, 20).until(expected_conditions.element_to_be_clickable((By.CLASS_NAME, 'submit-submission')))
    browser.find_element(By.CLASS_NAME, 'submit-submission').click()
    WebDriverWait(browser,20).until(expected_conditions.visibility_of_element_located((By.CSS_SELECTOR,'.smart-hints__hint')))
    response_message = browser.find_element(By.CSS_SELECTOR,'.smart-hints__hint').text
    assert 'Correct!' in response_message, f"Должно быть Correct!, а получилось {response_message}"


