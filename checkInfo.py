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

def checkJob(nickname):
    print('checkJob')
    url = 'https://maplestory.nexon.com/Ranking/World/Total?c='+nickname+'&w=0'
    raw = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text,"html.parser")
    try:
        job = html.select_one("tr.search_com_chk > td.left > dl > dd").text
        typeOfJob, job = job.split(' / ')

    except:
        typeOfJob = "Unknown"
        job = "Unknown"
    return typeOfJob, job

def checkLevel(nickname):
    url = 'https://maplestory.nexon.com/Ranking/World/Total?c='+nickname+'&w=0'
    raw = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text,"html.parser")
    try:
        level = html.select_one("tr.search_com_chk > td:nth-child(3)").text
        level = level.strip("Lv.")
    except:
        level = "Unknown"
    return level

def checkEXP(nickname):
    url = 'https://maplestory.nexon.com/Ranking/World/Total?c='+nickname+'&w=0'
    raw = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text,"html.parser")
    try:
        exp = html.select_one("tr.search_com_chk > td:nth-child(4)").text
    except:
        exp = "Unknown"
    return exp

def checkMuLung():
    return

def checkUnion(nickname):
    url = 'https://maplestory.nexon.com/Ranking/Union?c='+nickname+'&w=0'
    raw = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text,"html.parser")
    try:
        union = html.select_one("tr.search_com_chk > td:nth-child(3)").text 
    except:
        union = "Unknown"
    return union

def checkPoPularity(nickname):
    url = 'https://maplestory.nexon.com/Ranking/World/Total?c='+nickname+'&w=0'
    raw = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text,"html.parser")
    try:
        popularity = html.select_one("tr.search_com_chk > td:nth-child(5)").text

    except:
        popularity = 'Unknown'

    return popularity

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

def checkForTracker(nickname): #tracker.py 에서 requests 횟수를 줄이기 위해 합침, checkUnion은 따로 호출함
    url = 'https://maplestory.nexon.com/Ranking/World/Total?c='+nickname+'&w=0'
    raw = requests.get(url,headers={'User-Agent':'Mozilla/5.0'})
    html = BeautifulSoup(raw.text,"html.parser")
    try:
        job_ = html.select_one("tr.search_com_chk > td.left > dl > dd").text
        typeOfJob, job = job_.split(' / ')
        level = html.select_one("tr.search_com_chk > td:nth-child(3)").text
        level = level.strip("Lv.")
        exp = html.select_one("tr.search_com_chk > td:nth-child(4)").text
        popularity = html.select_one("tr.search_com_chk > td:nth-child(5)").text

    except:
        print('Fail on getting Info')

    return job, level, exp, popularity

