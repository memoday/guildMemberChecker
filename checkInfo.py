from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import sys, os

# options = webdriver.ChromeOptions()
# options.add_experimental_option("excludeSwitches", ["enable-logging"])
# options.add_argument('User-Agent= Mozilla/5.0')
# options.add_argument('headless') #크롬창 표시 금지

# def resource_path(relative_path):
#     """ Get absolute path to resource, works for dev and for PyInstaller """
#     base_path = getattr(sys, '_MEIPASS', os.path.dirname(os.path.abspath(__file__)))
#     return os.path.join(base_path, relative_path)

# driver_path = resource_path('chromedriver.exe')
# driver = webdriver.Chrome(options=options, executable_path=driver_path)

def checkJob():
    return

def checkLevel():
    return

def checkMuLung():
    return

def checkUnion():
    return

def checkGuild(nickname, guildName):
    url = 'https://maplestory.nexon.com/Ranking/World/Total?c='+nickname
    raw = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text,"html.parser")
    try:
        newGuild = html.select_one("tr.search_com_chk > td:nth-child(6)").text

        if newGuild != guildName:
            return False, newGuild
        return True,newGuild
    except AttributeError:
        return True, guildName

def checkGuildByExcel(nickname,guildName):
    return

def checkAchievements():
    return

