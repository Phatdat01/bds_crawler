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

def access_web(need:str, province:str, url:str, driver:WebDriver):
    driver.get(url=url)
    wait = wait_element(driver=driver,timeout=120,key="css",by=".uk-form-controls > .need > select")
 
    wait =driver.find_elements(By.CSS_SELECTOR,value=".uk-form-controls > .need > select")
    need_select = Select(wait[0])
    need_select.select_by_visible_text(need)
    wait =driver.find_elements(By.CSS_SELECTOR,value=".uk-form-controls > .city > select")
    need_select = Select(wait[0])
    need_select.select_by_visible_text(province)
    search = driver.find_elements(By.CSS_SELECTOR, value=".button > .uk-button")
    search[0].click()


def wait_element(driver: WebDriver, timeout: int, key: str, by: str) -> WebElement:
    if by.lower() == "id":
        condition = EC.presence_of_element_located((By.ID, key))
    elif by.lower() == "class":
        condition = EC.visibility_of_element_located((By.CLASS_NAME, key))
    elif by.lower() == "name":
        condition = EC.element_to_be_clickable((By.NAME, key))
    elif by.lower() == "tag":
        condition = EC.element_to_be_clickable((By.TAG_NAME, key))
    elif by.lower() == "css":
        condition = EC.element_to_be_clickable((By.CSS_SELECTOR, key))
    else:
        return []

    try:
        element = WebDriverWait(driver, timeout).until(condition)
        return element
    except:
        return []