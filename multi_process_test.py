from selenium import webdriver
import threading
from soupsieve.css_parser import ATTR

def browser1(url):
    browser = webdriver.Chrome(executable_path='chromedriver_win32/chromedriver.exe')
    browser.get(url)
    
if __name__ == "__main__":
    urls = ["https://gist.github.com/kurozumi/db763537c03d2ebbc3f53e1485e207c2", "http://ja.pymotw.com/2/threading/"]
    th1 = threading.Thread(target=browser1, args=([urls[0]]))
    th2 = threading.Thread(target=browser1, args=([urls[1]]))

    th1.start()
    th2.start()
