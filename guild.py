import time
from selenium import webdriver
import os, sys
import requests
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('User-Agent= Mozilla/5.0')
# options.add_argument('headless') #크롬창 표시 금지

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
driver_path = resource_path('chromedriver.exe')


driver = webdriver.Chrome(options=options, executable_path=driver_path)

def guildCrawl():
    global members

    print('guildCrawl')
    nowURL = driver.current_url
    raw = requests.get(nowURL, headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text,"html.parser")
    members = html.select("tbody > tr")

    try:
        for membersIndex in range(20):
            member = members[membersIndex].select_one('td.left > span > img')
            print(member)
    
    except IndexError:
        print(IndexError)

def getServer(articleIndex):

        server = articles[articleIndex].select_one('a > span > img')['src']
        
        print('getServer Returned')
        time.sleep(1)
        
        return server

def main(serverName, guildName):
    driver.get("https://maplestory.nexon.com/Ranking/World/Guild")

    driver.find_element_by_name('search_text').send_keys(guildName)
    driver.find_element_by_xpath('//*[@id="container"]/div/div/div[2]/div/span[1]/span').click()
    time.sleep(1)
    
    while True:
        global articles

        nowURL = driver.current_url
        raw = requests.get(nowURL,headers={'User-Agent':'Mozilla/5.0'})
        html = BeautifulSoup(raw.text,"html.parser")

        articles = html.select("#container > div > div > div:nth-child(4) > div.rank_table_wrap > table > tbody > tr")

        try:
            for articleIndex in range(10):
                nowServer = getServer(articleIndex)
                if 'icon_4' in nowServer:
                    driver.find_element_by_xpath('//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr['+str(articleIndex+1)+']/td[2]/span/a').click()
                    time.sleep(1)
                    guildCrawl()
                    break
        except IndexError:
            print('데이터가 더이상 없습니다')
            break
        
        print('while 탈출')
        break

if __name__ == "__main__":
    main("오로라",'MOON')
