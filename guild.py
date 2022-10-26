import time
from selenium import webdriver
import os, sys
import requests
from bs4 import BeautifulSoup
import openpyxl
import datetime
from PyQt5 import uic
from PyQt5.QtGui import *

options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument('User-Agent= Mozilla/5.0')
options.add_argument('headless') #크롬창 표시 금지

def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
    return os.path.join(base_path, relative_path)
driver_path = resource_path('chromedriver.exe')

driver = webdriver.Chrome(options=options, executable_path=driver_path)

def checkServer(serverName):
    icon = [None,None,'리부트','리부트2','오로라','레드','이노시스','유니온','스카니아','루나','제니스','크로아','베라','엘리시움','아케인','노바']
    iconNumber = icon.index(serverName)

    return iconNumber

def fileCreate(serverName, guildName):
    global ws1,wb,fileName
    now = datetime.datetime.now()
    
    now = now.strftime('%Y-%m-%d')

    fileName = serverName+'_'+guildName+'_'+now+'.xlsx'
    try:
        wb = openpyxl.load_workbook(fileName)
        print('file exists')
    except FileNotFoundError:
        print('File Not Found:')
        wb = openpyxl.Workbook()
    ws1 = wb.active

def guildCrawl():

    page = 1
    membersCount = 0

    nowURL = driver.current_url

    while True:

        newURL = nowURL+'&orderby=0&page='+str(page)+''
        raw = requests.get(newURL,headers={'User-Agent':'Mozilla/5.0'})
        html = BeautifulSoup(raw.text,"html.parser")   
        members = html.select('#container > div > div > table > tbody > tr')
        
        for member in range(20):
            membersCount += 1
            nickName = members[member].select_one('td.left > dl > dt > a').text
            print(nickName)
            ws1.append([nickName])
        page += 1

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
                if 'icon_'+str(checkServer(serverName))+'' in nowServer:
                    driver.implicitly_wait(5)

                    driver.find_element_by_xpath('//*[@id="container"]/div/div/div[3]/div[1]/table/tbody/tr['+str(articleIndex+1)+']/td[2]/span/a').click()
                    driver.implicitly_wait(5)

                    driver.switch_to.window(driver.window_handles[-1])
                    driver.implicitly_wait(5)

                    fileCreate(serverName, guildName)
                    guildCrawl()
                    break
        except IndexError:
            print('데이터가 더이상 없습니다.')
            wb.save(fileName)
            break
        
        print('while 탈출')
        wb.save(fileName)
        break

if __name__ == "__main__":
    print('서버 입력')
    serverName = input()
    print('길드 입력')
    guildName = input()
    main(serverName,guildName)
