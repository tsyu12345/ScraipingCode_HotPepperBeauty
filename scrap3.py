from openpyxl.worksheet.dimensions import SheetDimension
from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException, InvalidSwitchToTargetException, NoSuchElementException, TimeoutException, WebDriverException
from selenium.webdriver.common.keys import Keys
from openpyxl import styles as pxstyle
import openpyxl as px
from bs4 import BeautifulSoup as bs
import time
import datetime
import re
import requests as rq
import threading as th

class Job:
    def __init__(self, driver_path, book_path, area, store_class):
        self.driver_path = driver_path
        self.book_path = book_path
        self.book = px.load_workbook(book_path)
        self.sheet = self.book.worksheets[0]
        self.area_name = area
        self.store_class = store_class
    
    def url_scrap(self):
        print("starting ChromeDriver.exe....")
        driver = webdriver.Chrome(executable_path=self.driver_path)
        driver.get("https://beauty.hotpepper.jp/top/")  # top page
        sr_class = driver.find_element_by_link_text(self.store_class)
        sr_class.click()
        time.sleep(1)
        search = driver.find_element_by_css_selector('#freeWordSearch1')
        search.send_keys(self.area_name + Keys.ENTER)
        time.sleep(2)
        result_count = driver.find_element_by_css_selector(
            '#mainContents > div.mT20.bgWhite > div.preListHead > div > p:nth-child(1) > span').text
        result_pages = driver.find_element_by_css_selector(
            '#mainContents > div.mT20.bgWhite > div.preListHead > div > p.pa.bottom0.right0').text
        page_num = re.split('[/ ]', result_pages)
        pages = re.sub(r"\D", "", page_num[1])
        print("Search Result : %s : %s" % (self.area_name, result_count))
        print("pages : " + pages)
        link_list = []
        for i in range(int(pages)):
            html = driver.page_source
            soup = bs(html, 'lxml')
            links_list = soup.select("div.slcHeadContentsInner > h3 > a")
            for a in links_list:
                url = a.get('href')
                link_list.append(url)
            try:
                next_btn = driver.find_element_by_link_text("次へ")
                next_btn.click()
                time.sleep(1)
            except NoSuchElementException:
                break
        print("search complete")

        for i in range(len(link_list)):
            self.sheet.cell(row=i+2, column=1, value=self.store_class)
            self.sheet.cell(row=i+2, column=8, value=link_list[i])
        self.book.save(self.book_path)
        driver.quit()
        

    def info_scrap(self, url_list, index):
        driver = webdriver.Chrome(executable_path=self.driver_path)
        


    def scrap_day(self):
        dt_now = datetime.datetime.now()
        year = str(dt_now.year)
        month = str(dt_now.month)
        day = str(dt_now.day)
        hour = str(dt_now.hour)
        min = str(dt_now.minute)
        data_day = year + "," + month + day + "," + hour + min
        print(data_day)
        return data_day
    