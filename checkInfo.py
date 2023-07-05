from bs4 import BeautifulSoup
import requests
from selenium import webdriver
import re

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

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Whale/3.18.154.13 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8"
}

def checkJob(nickname):
    print('checkJob')
    url = 'https://maplestory.nexon.com/Ranking/World/Total?c='+nickname+'&w=0'
    raw = requests.get(url,headers=header)
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
    raw = requests.get(url,headers=header)
    html = BeautifulSoup(raw.text,"html.parser")
    try:
        level = html.select_one("tr.search_com_chk > td:nth-child(3)").text
        level = level.strip("Lv.")
    except:
        level = "0"
    return level

def checkEXP(nickname):
    url = 'https://maplestory.nexon.com/Ranking/World/Total?c='+nickname+'&w=0'
    raw = requests.get(url,headers=header)
    html = BeautifulSoup(raw.text,"html.parser")
    try:
        exp_ = html.select_one("tr.search_com_chk > td:nth-child(4)").text
        exp = exp_.replace(',','')
    except:
        exp = "0"
    return exp

def checkMuLung():
    return

def checkUnion(nickname):
    url = 'https://maplestory.nexon.com/Ranking/Union?c='+nickname+'&w=0'
    raw = requests.get(url,headers=header)
    html = BeautifulSoup(raw.text,"html.parser")
    try:
        union_ = html.select_one("tr.search_com_chk > td:nth-child(3)").text 
        union = union_.replace(',',"")
    except:
        union = "0"
    return union

def checkPoPularity(nickname):
    url = 'https://maplestory.nexon.com/Ranking/World/Total?c='+nickname+'&w=0'
    raw = requests.get(url,headers=header)
    html = BeautifulSoup(raw.text,"html.parser")
    try:
        popularity_ = html.select_one("tr.search_com_chk > td:nth-child(5)").text
        popularity = popularity_.replace(',','')

    except:
        popularity = '0'

    return popularity

def checkGuild(nickname, guildName):
    url = 'https://maplestory.nexon.com/Ranking/World/Total?c='+nickname
    raw = requests.get(url,headers=header)
    html = BeautifulSoup(raw.text,"html.parser")
    try:
        newGuild = html.select_one("tr.search_com_chk > td:nth-child(6)").text

        if newGuild != guildName:
            return False, newGuild
        return True,newGuild
    except AttributeError:
        return True, guildName

def checkAchievements():
    return

def checkAllGG(nickname):
    url = 'https://maple.gg/u/'+nickname
    raw = requests.get(url,headers=header)
    html = BeautifulSoup(raw.text,"html.parser")
    try:

        job = html.select_one('#user-profile > section > div.row.row-normal > div.col-lg-8 > div.user-summary > ul > li:nth-child(2)').text

        level_ = html.select_one("#user-profile > section > div.row.row-normal > div.col-lg-8 > div.user-summary > ul > li:nth-child(1)").text
        level = level_.strip("Lv.")
        to_clean = re.compile(r'\([^)]*\)')
        level = re.sub(to_clean,'',level)

        popularity_ = html.select_one('#user-profile > section > div.row.row-normal > div.col-lg-8 > div.user-summary > ul > li:nth-child(3) > span:nth-child(2)').text
        popularity = popularity_.replace(',','')
    
    except:
        print('Failed on getting Info: '+nickname)
        return 'Not Found'

    try:
        union_ = html.select_one('#app > div.card.border-bottom-0 > div > section > div.row.text-center > div:nth-child(3) > section > div > div > span').text
        union = union_.strip("Lv.")
    except:
        union = '0'

    return job, level,popularity, union
    
def checkForTracker(nickname): #tracker.py 에서 requests 횟수를 줄이기 위해 합침, checkUnion은 따로 호출함
    url = 'https://maplestory.nexon.com/Ranking/World/Total?c='+nickname+'&w=0'
    raw = requests.get(url,headers=header)
    html = BeautifulSoup(raw.text,"html.parser")
    try:
        job_ = html.select_one("tr.search_com_chk > td.left > dl > dd").text
        typeOfJob, job = job_.split(' / ')
        level = html.select_one("tr.search_com_chk > td:nth-child(3)").text
        level = level.strip("Lv.")
        popularity = html.select_one("tr.search_com_chk > td:nth-child(5)").text
        union = checkUnion(nickname)

    except UnboundLocalError:
        return 'Not Found'
    except:
        print('Failed on getting Info: '+nickname)
        return 'Not Found'

    return job, level, popularity, union