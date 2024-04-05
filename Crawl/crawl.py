from storing import store_data
from crawling import load_chrome, access_web, collect_data
import time

URL = "https://batdongsan.vn/"

def crawling():
    driver = load_chrome()
    access_web(need="Bán", province="Long An", url=URL, driver=driver)
    data = collect_data(driver)
    print(data)
    store_data(data=data,link=".",name="temp")
    driver.close()

crawling()