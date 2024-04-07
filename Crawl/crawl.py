from pathlib import Path
from storing import store_data
from crawling import load_chrome, access_web, collect_data, change_page
import time

URL = "https://batdongsan.vn/"
DOWNLOAD_PATH = str(Path.home() / "Downloads")

def crawling(need: str, province: str, page: int, donwload_folder: str, file_name: str):
    try:
        driver = load_chrome()
        access_web(need=need, province=province, url=URL, page=page, driver=driver)
        page=1
        while True:
            data = collect_data(driver,page=str(page),need=need, province=province, href=URL)
            store_data(data=data, link=donwload_folder, file_name=file_name)
            if not change_page(driver=driver):
                break
            page += 1
    except:
        pass
    finally:
        # Close the driver even if an exception is raised
        driver.quit()

crawling(need="Bán", province="Long An", page=3, donwload_folder=DOWNLOAD_PATH, file_name="temp")