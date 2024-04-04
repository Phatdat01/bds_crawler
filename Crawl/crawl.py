from crawling import load_chrome, access_web

URL = "https://batdongsan.vn/"
def crawling():
    driver = load_chrome()
    access_web(need="Bán", province="Long An", url=URL, driver=driver)


crawling()