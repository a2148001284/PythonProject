import sys
sys.path.append("./package")
from selenium import webdriver
import requests
import time
from selenium.webdriver.common.action_chains import ActionChains

def web_driver():
    options=webdriver.ChromeOptions()
    location = r"C:/Users/86181/Desktop/python/python和爬虫/chrome-win/chrome.exe"
    options.binary_location = location
    #options.add_argument("headless")
    #mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
    #options.add_experimental_option('mobileEmulation', mobileEmulation)
    driver = webdriver.Chrome("C:/Users/86181/Desktop/python/python和爬虫/chromedriver.exe", options=options)
    return driver

def main():
    url="http://i.nuist.edu.cn/qljfwapp/sys/lwNuistHealthInfoDailyClock/index.do#/healthClock"
    headers={
        "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.102 Safari/537.36"
    }
    code=requests.get(url=url,headers=headers).status_code
    if code !=200 :
        print("Error! Access Failed!")
        return
    driver=web_driver()
    driver.get(url)
    time.sleep(1)
    #login=driver.find_element_by_xpath("//div[@class='bh-btn bh-btn-primary']")
    #ActionChains(driver).click(login).perform()


    time.sleep(6)
    driver.quit()
    print("Connect Success!")


if __name__ == '__main__':
    main()
