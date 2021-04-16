from os import cpu_count
from openpyxl.worksheet.dimensions import SheetDimension
from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from openpyxl import styles as pxstyle
import openpyxl as px 
from bs4 import BeautifulSoup as bs 
import time
import re
import requests as rq

class Job:

    def __init__(self, driver_path, books_path):
        self.book_path = books_path
        self.book = px.load_workbook(books_path)
        self.sheet = self.book.worksheets[0]
        self.driver = webdriver.Chrome(executable_path=driver_path)
    
    def scrap(self, area_name):
        print("starting ChromeDriver.exe....")
        self.driver.get("https://beauty.hotpepper.jp/")#top page
        search = self.driver.find_element_by_css_selector('#freeWordSearch1')
        search.send_keys(area_name + Keys.ENTER)
        time.sleep(2)
        result_count = self.driver.find_element_by_css_selector('#mainContents > div.mT20.bgWhite > div.preListHead > div > p:nth-child(1) > span').text 
        result_pages = self.driver.find_element_by_css_selector('#mainContents > div.mT20.bgWhite > div.preListHead > div > p.pa.bottom0.right0').text
        page_num = re.split('[/ ]', result_pages)
        pages = re.sub(r"\D", "", page_num[1])
        print("Search Result : %s : %s" % (area_name, result_count))
        print("pages : " + pages)
        link_list = []
        for i in range(2):
            html = self.driver.page_source
            soup = bs(html, 'lxml')
            links_list = soup.select("div.slcHeadContentsInner > h3 > a")
            for a in links_list:
                url = a.get('href')
                link_list.append(url)
            next_btn = self.driver.find_element_by_link_text("次へ")
            next_btn.click()
            time.sleep(1)
        print("search complete")
        for i in range(len(link_list)):
            self.sheet.cell(row=i+2, column=8, value=link_list[i])
        self.book.save(self.book_path)
#mainContents > ul > li:nth-child(1) > div.slcHeadWrap.cFix > div > div.slcHeadContentsInner > h3 > a
job = Job("chromedriver_win32\chromedriver.exe", "【サンプル】ホットペッパービューティー - コピー.xlsx")
job.scrap("北海道")



        

       