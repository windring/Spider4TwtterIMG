# -*- coding: UTF-8 -*-
import unittest
from selenium import webdriver
from bs4 import BeautifulSoup
import os
import time
import urllib

class seleniumTest(unittest.TestCase):
    def setUp(self):
        print("start")
        self.driver=webdriver.PhantomJS()
        self.driver.implicitly_wait(20)
        self.driver.set_window_size('1280', '768')
        self.driver.maximize_window()
        self.endselector="stream-end-inner"
        self.cardselector=".js-stream-item.stream-item.stream-item"
        self.imgselector={"src": True, "data-aria-label-part": True}
        self.username="ruru2333"
    def testEle(self):
        driver=self.driver
        username=self.username
        endselector=self.endselector
        cardselector=self.cardselector
        imgselector=self.imgselector
        if os.path.isdir("./"+username)==False:
            os.mkdir("./"+username)
        driver.get("https://twitter.com/"+username+"/media")
        len1=0
        len2=0
        count=0
        while(1):
            driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
            print(time.time())
            soup = BeautifulSoup(driver.page_source, "html.parser")
            soup_re = soup.findAll("img",imgselector )
            if(soup_re and len(soup_re)>len2):
                for imgs in soup_re[len2-1:len(soup_re)]:
                    print(imgs['src'])
                    u = urllib.request.urlopen(imgs['src'] + ":large")
                    data = u.read()
                    f = open("./"+username+"/"+str(count)+"-"+imgs['src'].split('/')[4], "wb")
                    f.write(data)
                    f.close()
                    count+=1
                    print(count)
            len1 = len(driver.find_elements_by_css_selector(cardselector))
            if(len(soup_re)>len2):
                len2=len(soup_re)
            print(len1,len2)
            if driver.find_element_by_class_name(endselector).is_displayed():
                #driver.save_screenshot("./"+username+"/end.png")
                print("last:",count)
                break
    def tearDown(self):
        self.driver.close()
        print('End')
if __name__ == "__main__":
    unittest.main()