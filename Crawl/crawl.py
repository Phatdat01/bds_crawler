from Crawl.storing import store_data
from Crawl.crawling import load_chrome, access_web, collect_data, change_page

URL = "https://batdongsan.vn/"

def crawl(need: str, province: str, page: int, donwload_folder: str, file_name: str):
    try:
        driver = load_chrome()
        access_web(need=need, province=province, url=URL, page=page, driver=driver)
        page=1
        while True:
            data = collect_data(driver,page=str(page),need=need, province=province, href=URL)
            if len(data):
                store_data(data=data, path=donwload_folder, file_name=file_name)
            if not change_page(driver=driver):
                break
            page += 1
    except:
        pass
    finally:
        # Close the driver even if an exception is raised
        driver.quit()