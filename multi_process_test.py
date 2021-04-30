from selenium import webdriver
import threading
from soupsieve.css_parser import ATTR

def browser1(v):
    """
    browser = webdriver.Chrome(executable_path='chromedriver_win32/chromedriver.exe')
    browser.get(url)
    """
    value = 1 + v
    print(value)
if __name__ == "__main__":
    urls = [1, 2, 3, 4, 5]
    th1 = threading.Thread(target=browser1, args=([urls[0]]))
    th2 = threading.Thread(target=browser1, args=([urls[3]]))

    th1.start()
    th2.start()
