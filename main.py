from os import cpu_count
import string
from openpyxl.worksheet.dimensions import SheetDimension
from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException, NoSuchElementException, TimeoutException
from selenium.webdriver.common.keys import Keys
from openpyxl import styles as pxstyle
import openpyxl as px 
from bs4 import BeautifulSoup as bs 
import time
import datetime
import re
import requests as rq

class Job:

    def __init__(self, driver_path, books_path):
        self.book_path = books_path
        self.book = px.load_workbook(books_path)
        self.sheet = self.book.worksheets[0]
        self.driver = webdriver.Chrome(executable_path=driver_path)
    
    def url_scrap(self, area_name, store_class):
        print("starting ChromeDriver.exe....")
        self.driver.get("https://beauty.hotpepper.jp/top/")#top page
        sr_class = self.driver.find_element_by_link_text(store_class)
        sr_class.click()
        time.sleep(1)
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
        for i in range(int(pages)):
            html = self.driver.page_source
            soup = bs(html, 'lxml')
            links_list = soup.select("div.slcHeadContentsInner > h3 > a")
            for a in links_list:
                url = a.get('href')
                link_list.append(url)
            try:
                next_btn = self.driver.find_element_by_link_text("次へ")
                next_btn.click()
                time.sleep(1)
            except NoSuchElementException:
                break
        print("search complete")
        #write excel
        for i in range(len(link_list)):
            self.sheet.cell(row=i+2, column=1, value=store_class)
            self.sheet.cell(row=i+2, column=8, value=link_list[i])
        self.book.save(self.book_path)
        

    def info_scrap(self, url, *index):
        now = datetime.datetime.now()
        year = str(now.year)
        month = str(now.month)
        day = str(now.day)
        hour = str(now.hour)
        min = str(now.min)
        data_day = year + "," + month + day + "," + hour + min
        headers = {"User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0"}
        respons = rq.get(url=url, headers=headers)
        print(url + " : ", end="")
        print(respons.status_code)
        html = respons.text
        soup = bs(html, 'lxml')
        store_name_tag = soup.select_one('p.detailTitle > a')
        store_name = store_name_tag.get_text()
        print("店名：" + store_name)
        st_name_kana_tag = soup.select_one('#mainContents > div.detailHeader.cFix.pr > div > div.pL10.oh.hMin120 > div > p.fs10.fgGray')
        st_name_kana = st_name_kana_tag.get_text()
        print("店名カナ：" + st_name_kana)
        tel_tag = soup.select_one('#mainContents > div:nth-child(12) > table > tr > td > a')
        tel_url = tel_tag.get('href')

        respons_tel = rq.get(tel_url)
        html_tel = respons_tel.text
        soup_tel = bs(html_tel, 'lxml')
        tel_num_tag = soup_tel.select_one('table > tr > td')
        tel = tel_num_tag.get_text()
        print("TEL : " + tel)
        
        table = soup.select('#mainContents > div:nth-child(12) > table > tr > td')
        all_address = table[1].get_text()
        prefecture_search = re.search('東京都|北海道|(?:京都|大阪)府|.{2,3}県' , all_address)
        address_low = re.split('東京都|北海道|(?:京都|大阪)府|.{2,3}県', all_address)#県名とそれ以降を分離
        prefecture = prefecture_search.group()#県名
        municipality = address_low[1]#それ以降
        print("都道府県：" + prefecture)
        print("市区町村番地：" + municipality)
        anounce_access = table[2].get_text()
        bs_time = table[3].get_text()
        holiday = table[4].get_text()
        credit = table[5].get_text()
        fee = table[6].get_text()
        seat_cnt = table[7].get_text()
        staff_cnt = table[8].get_text()
        parking = table[9].get_text()
        commitment = table[10].get_text()
        remarks = table[11].get_text()

        catch_copy_tag = soup.select_one('#mainContents > div.pH10.mT25 > div:nth-child(1) > p > b > strong')
        catch_copy = catch_copy_tag.get_text()

        pankuzu_tag = soup.select('#preContents > ol > li')
        pankuzu = ""
        for pan in pankuzu_tag:
            pankuzu += pan.get_text()
        print(pankuzu)

        slide_img_tag = soup.select('#mainContents > div.pH10.mT25 > div:nth-child(1) > div > div.slnTopImg.jscThumbCarousel > div.slnTopImgCarouselWrap.jscThumbWrap > ul > li')
        slide_cnt = len(slide_img_tag)
 
        #store_name
        self.sheet.cell(row=index, column=2, value=str(store_name))
        self.sheet.cell(row=index, column=3, value=st_name_kana)
        self.sheet.cell(row=index, column=4, value=tel)
        self.sheet.cell(row=index, column=6, value=prefecture)
        self.sheet.cell(row=index, column=7, value=municipality)
        self.sheet.cell(row=index, column=9, value=data_day)
        self.sheet.cell(row=index, column=13, value=pankuzu)
        self.sheet.cell(row=index, column=16, value=slide_cnt)
        self.sheet.cell(row=index, column=17, value=catch_copy)
        self.sheet.cell(row=index, column=18, value=anounce_access)
        self.sheet.cell(row=index, column=19, value=bs_time)
        self.sheet.cell(row=index, column=20, value=holiday)
        self.sheet.cell(row=index, column=21, value=credit)
        self.sheet.cell(row=index, column=23, value=fee)
        self.sheet.cell(row=index, column=24, value=seat_cnt)
        self.sheet.cell(row=index, column=25, value=staff_cnt)
        self.sheet.cell(row=index, column=26, value=parking)
        self.sheet.cell(row=index, column=27, value=commitment)
        self.sheet.cell(row=index, column=28, value=remarks)
        self.book.save(self.book_path)


book = px.load_workbook("【サンプル】ホットペッパービューティー - コピー.xlsx")
sheet = book.worksheets[0]
job = Job("chromedriver_win32\chromedriver.exe", "【サンプル】ホットペッパービューティー - コピー.xlsx")
job.url_scrap("北海道", "ヘアサロン")
for i in range(sheet.max_row):
    job.info_scrap(sheet.cell(row=i+2, column=8).value, i+2)
book.save("【サンプル】ホットペッパービューティー - コピー.xlsx")



        

       