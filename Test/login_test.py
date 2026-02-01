import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.webdriver import WebDriver


def test_login(): #possitive case
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    time.sleep(5)
    driver.find_element(By.NAME,"user-name").send_keys("standard_user")
    driver.find_element(By.NAME,"password").send_keys("secret_sauce")
    driver.find_element(By.ID,"login-button").click()

def test_login_incorrect(): #negative testcase
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    time.sleep(5)
    driver.find_element(By.NAME,"user-name").send_keys("abc_user")
    driver.find_element(By.NAME,"password").send_keys("abc_sauce")
    driver.find_element(By.ID,"login-button").click()

def test_get_title_url():
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    time.sleep(5)
    actual_title = driver.title
    assert actual_title == "Swag Labs" ,"this is not as Expected title"
    actual_url = driver.current_url
    assert actual_url == "https://www.saucedemo.com/", "URL is not as expected Url"

def test_extract_data():
    driver = webdriver.Edge()
    driver.get("https://www.saucedemo.com/")
    text = driver.find_element(By.TAG_NAME, "html").text
    print(text)
