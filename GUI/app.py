import tkinter as tk
from tkinter import ttk 
from tkinter import messagebox
from pathlib import Path

from Crawl.crawl import crawl

NEED_LIST = [
    "Bán",
    "Cho thuê"
]

PROVINCE_LIST = [
    "An Giang","Bà Rịa Vũng Tàu","Bạc Liêu","Bắc Kạn","Bắc Giang","Bắc Ninh","Bến Tre","Bình Dương","Bình Định","Bình Phước","Bình Thuận","Cà Mau","Cần Thơ",
    "Cao Bằng","Đà Nẵng","Đắk Lắk","Đắk Nông","Điện Biên","Đồng Nai","Đồng Tháp","Gia Lai","Hà Giang","Hà Nam","Hà Nội","Hà Tĩnh","Hải Dương","Hải Phòng",
    "Hậu Giang","Hòa Bình","Hưng Yên","Khánh Hòa","Kiên Giang","Kon Tum","Lai Châu","Lâm Đồng","Lạng Sơn","Lào Cai","Long An","Nam Định","Nghệ An","Ninh Bình",
    "Ninh Thuận","Phú Thọ","Phú Yên","Quảng Bình","Quảng Nam","Quảng Ngãi","Quảng Ninh","Quảng Trị","Sóc Trăng","Sơn La","Tây Ninh","Thái Bình","Thái Nguyên",
    "Thanh Hóa","Thừa Thiên Huế","Tiền Giang","TP Hồ Chí Minh","Trà Vinh","Tuyên Quang","Vĩnh Long","Vĩnh Phúc","Yên Bái"
]

PAGE_LIST = list(range(1, 1001))

DOWNLOAD_PATH = str(Path.home() / "Downloads")
FILE_NAME="temp"

def start_crawl(need: str, province: str, page: int):
    crawl(need=need, province=province, page=page, donwload_folder=DOWNLOAD_PATH, file_name=FILE_NAME)

def process_theme():
    """
    process click button take value from combo box

    Returns:
        None
    """  

    win = tk.Tk()

    ttk.Label(win, text = "batdongsan.vn",
        font = ("Times New Roman", 20, "bold")).grid(column = 1, 
        row = 1, columnspan=2, padx = 10, pady = 10)

    # Label of textbox:
    ttk.Label(win, text = "Nhu cầu:", width = 10,
        font = ("Times New Roman", 15)).grid(column = 1, 
        row = 2, padx = 10, sticky="w")
    ttk.Label(win, text = "Tỉnh:", width = 10,
        font = ("Times New Roman", 15)).grid(column = 2, 
        row = 2, padx = 10, sticky="w")

    # need Texbox
    need = ttk.Combobox(win, width = 10, font=25, textvariable = tk.Listbox(), state="readonly")
    need['values'] = NEED_LIST
    need.grid(column = 1, row = 3, padx = 20,pady=10) 
    need.current(0)

    # province
    province = ttk.Combobox(win, width = 10, font=25, textvariable = tk.Listbox(), state="readonly")
    province['values'] = PROVINCE_LIST
    province.grid(column = 2, row = 3, padx = 20,pady=10) 
    province.current(0)

    ttk.Label(win, text = "Page:", 
        font = ("Times New Roman", 15)).grid(column = 1, 
        row = 4, padx = 10, pady = 10, sticky="e")
    # page number
    page = ttk.Combobox(win, width = 10, font=25, textvariable = tk.Listbox())
    page['values'] = PAGE_LIST
    page.grid(column = 2, row = 4, padx = 20,pady=10) 
    page.current(0)

    # action
    start=tk.Button(
        win,
        text = "Run",
        bg = "green",
        font = "25",
        width = 10, 
        cursor="hand2",
        command = lambda: start_crawl(
            need=need.get(),
            province=province.get(),
            page=page.get()
        ) 
    )
    start.grid(row=5, column=1, columnspan=2, padx = 20,pady=10)

    win.eval('tk::PlaceWindow . center')
    win.mainloop()