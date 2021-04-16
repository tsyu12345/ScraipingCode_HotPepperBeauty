from openpyxl.worksheet.dimensions import SheetDimension
from selenium import webdriver
from selenium.common.exceptions import InvalidArgumentException, NoSuchElementException, TimeoutException
from openpyxl import styles as pxstyle
import openpyxl as px 
from bs4 import BeautifulSoup as bs 
import time
from selenium.webdriver.common.keys import Keys

class Job:

    def __init__(self, driver_path, books_path):
        self.book = px.load_workbook(books_path)
        self.sheet = self.book.worksheets[0]
        self.driver = webdriver.Chrome(executable_path=driver_path)
    
    def scrap(self, *area_name, url):
        print("starting ChromeDriver.exe....")
        self.driver.get(url)#top page
        

       