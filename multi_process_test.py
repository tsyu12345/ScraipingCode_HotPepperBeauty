from selenium import webdriver
import threading

from soupsieve.css_parser import ATTR

def browser1(urls):
    browser = webdriver.Chrome(executable_path='chromedriver_win32/chromedriver.exe')
    for i in range(len(urls)):
        browser.get(urls[i])
    



if __name__ == "__main__":
    urls1 = ["https://gist.github.com/kurozumi/db763537c03d2ebbc3f53e1485e207c2", "http://ja.pymotw.com/2/threading/", "https://qiita.com/tchnkmr/items/b05f321fa315bbce4f77", "https://qiita.com/str416yb/items/0623d6089d4ea821d0eb"]
    th1=threading.Thread(target=browser1, args=([urls1[0:2]]))
    th2=threading.Thread(target=browser1, args=([urls1[2:4]]))
   
    th1.start()
    th2.start()
