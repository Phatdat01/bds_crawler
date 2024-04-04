from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def load_chrome() -> WebDriver:
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def access_web(nees:str, province:str, url:str, driver:WebDriver):
    driver.get(url=url)
    wait = wait_element(driver=driver,timeout=120,key="css",by=".uk-form-controls > .need > select")


def wait_element(driver: WebDriver, timeout: int, key:str, by:str) -> WebElement:
    if by.lower() == "id":
        condition = EC.visibility_of_element_located((By.ID, key))
    elif by.lower() == "class":
        condition = EC.visibility_of_element_located((By.CLASS_NAME, key))
    elif by.lower() == "name":
        condition = EC.visibility_of_element_located((By.NAME, key))
    elif by.lower() == "tag":
        condition = EC.visibility_of_element_located((By.TAG_NAME, key))
    elif by.lower() == "css":
        condition = EC.visibility_of_element_located((By.CSS_SELECTOR, key))
    else:
        return []

    element = WebDriverWait(driver, timeout).until(condition)
    return element