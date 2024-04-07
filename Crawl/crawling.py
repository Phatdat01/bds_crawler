import time
import pandas as pd
from typing import List

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support import expected_conditions as EC

def load_chrome() -> WebDriver:
    service = Service()
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=options)
    return driver

def access_web(need:str, province:str, url:str, page: int, driver:WebDriver):
    driver.get(url=url)

    time.sleep(4)
    ## witch to just same 1
    action_with_multi_case(driver=driver,css_selector_list=["a > .uk-icon-search", ".button > .uk-button"])    
    ## Fill to Need (Nhu Cầu)
    wait = wait_element(driver=driver,timeout=5,key=".uk-form-controls", by="class")
    need_box = driver.find_elements(By.CSS_SELECTOR,value=".uk-form-controls > .need > select")
    handle_tag(taglist=need_box, content=need)

    time.sleep(0.2)
    ## Fill to province
    province_box = driver.find_elements(By.CSS_SELECTOR,value=".uk-form-controls > .city > select")
    handle_tag(taglist=province_box, content=province)
    
    time.sleep(1)
    ## Click
    searchs = driver.find_elements(By.CSS_SELECTOR, value=".button > .uk-button")
    handle_tag(taglist=searchs)
    if page != 1:
        time.sleep(4)
        driver.get(f"{driver.current_url}/p{page}")

def change_page(driver: WebDriver):
    time.sleep(0.5)
    next = driver.find_element(By.CSS_SELECTOR,value='[rel="next"]')
    if next:
        next.click()
        content_page = wait_element(driver=driver, timeout=10, key="datalist", by="class")
        return True
    return False

def collect_data(driver: WebDriver, page: str,need: str, province: str, href: str):
    new_data = pd.DataFrame(columns= ["page","item","need","province","price","area","address","customer_name","customer_link","customer_mail","customer_phone","content","img"])
    new_data["customer_phone"] = new_data["customer_phone"].astype(str)
    content_page = driver.find_elements(By.CLASS_NAME,value="datalist")[0]
    urls = content_page.find_elements(By.CSS_SELECTOR, 'div > div > .item > .image.cover > a')
    # for index in range(len(urls),4):
    pass_item =1
    for index in range(len(urls)):
        row = {}
        ## Open new tab
        ## open web
        try:
            url=urls[index].get_attribute("href")
            driver.execute_script("window.open('');")
            driver.switch_to.window(driver.window_handles[1])
            driver.get(url=url)
            wait = wait_element(driver=driver,timeout=5,key=".body > .meta > strong",by="css")
            if href != driver.current_url:
                check = driver.find_elements(By.CSS_SELECTOR,value=".param > .uk-list > li")[0].text
                if "diện tích" in check.lower():
                    try:
                        row["page"] = page
                        row["item"] = pass_item
                        row["need"] = need
                        row["province"]= province
                        row["area"] = check.replace("Diện tích: ","")
                        row["price"] = get_value_with_css_selector(driver=driver, item=".body > .meta > strong")                      
                        row["address"] = get_value_with_css_selector(driver=driver, item=".param > .uk-list > li", index_of_list=1)
                        row["content"] = get_value_with_css_selector(driver=driver, item=".body > .content")
                        row["customer_name"] = get_value_with_css_selector(driver=driver, item=".header > .name > a")
                        row["customer_link"] = get_value_with_css_selector(driver=driver, item=".header > .name > a", is_url=True)
                        row["customer_mail"] = get_value_with_css_selector(driver=driver, item=".more.email > a", is_url=True)
                        row["customer_phone"] = get_value_with_css_selector(driver=driver, item=".more.phone > a", is_url=True)
                    except:
                        pass
                    ## list of img link
                    img_links= driver.find_elements(By.CSS_SELECTOR,value=".uk-slider-container > div > div > .image.cover > a")
                    row["img"] = [link.get_attribute("href") for link in img_links]    
                    new_data.loc[len(new_data)] = row
                    pass_item +=1

            driver.execute_script("window.close();")
            driver.switch_to.window(driver.window_handles[0])
            print(driver.window_handles)
        except:
            pass
    return new_data


def get_value_with_css_selector(driver: WebDriver, item: str, is_url: bool=False, index_of_list: int=None):
    words_to_remove = ["mailto:", "tel:"]
    try:
        if index_of_list:
            return driver.find_elements(By.CSS_SELECTOR, value=item)[index_of_list].text
        result = driver.find_element(By.CSS_SELECTOR, value=item)
        if is_url:
            result = result.get_attribute("href")
        else:
            result = result.text
        for word in words_to_remove:
            result = result.replace(word,"")
        return result
    except:
        return ""

def action_with_multi_case(driver:WebDriver, css_selector_list: List[str]):
    for css_selector in css_selector_list:
        try:
            search = driver.find_elements(By.CSS_SELECTOR, value=css_selector)
            handle_tag(taglist=search)
        except:
            pass

def handle_tag(taglist: List[WebDriver], index: int = None, content: str = ""):
    if index == None:
        index = len(taglist)-1
    try:
        handle_tag_action(taglist=taglist, index=index, content=content)
    except Exception as e:
        # Handle specific exceptions as per your requirement
        if index != 0:
            handle_tag(taglist=taglist, index=index-1, content=content)

def handle_tag_action(taglist: List[WebDriver],index: int, content : str = ""):
    if content:
        need_select = Select(taglist[index])
        need_select.select_by_visible_text(content)
    else:
        taglist[index].click()


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