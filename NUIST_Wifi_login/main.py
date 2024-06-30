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
    options.add_argument("headless")
    mobileEmulation = {'deviceName': 'iPhone 6/7/8'}
    options.add_experimental_option('mobileEmulation', mobileEmulation)
    driver = webdriver.Chrome("C:/Users/86181/Desktop/python/python和爬虫/chromedriver.exe", options=options)
    return driver

def main():
    url="http://10.255.255.34/authentication"
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
    #ActionChains(driver).move_by_offset(100,252).click().perform()
    driver.find_element_by_id("login-pc_username").send_keys("18115129239")
    driver.find_element_by_id("login-pc_password").send_keys("320057")
    time.sleep(1)
    login=driver.find_element_by_xpath("//button[@class='login-form-button ant-btn ant-btn-primary']")
    ActionChains(driver).click(login).perform()
    time.sleep(1)
    target=driver.find_element_by_xpath("//button[@class='col ant-btn ant-btn-lg ant-btn-block']/span[contains(text(),'中国电信')]")
    ActionChains(driver).click(target).perform()
    time.sleep(6)
    driver.quit()
    print("Connect Success!")


if __name__ == '__main__':
    main()