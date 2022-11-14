import checkInfo as ci
import requests
from bs4 import BeautifulSoup

def tracker(trackingNick, newNickList):

    global info

    nickInfoList = []
    maybe = [] #닉변 유력 후보

    union = ci.checkUnion(trackingNick)
    nickInfoList = ci.checkForTracker(trackingNick)
    info = {
        "job" : nickInfoList[0],
        "level" : nickInfoList[1],
        "exp" : nickInfoList[2],
        "popularity" : nickInfoList[3],
        "union" : union
    }

    for i in range(len(newNickList)):
        check = compare(trackingNick,newNickList[i])
        if check == 'maybe':
            maybe.append(newNickList[i])
    
    return maybe

def compare(trackingNick, newNick):


    union2 = ci.checkUnion(newNick)
    nickInfoList2 = ci.checkForTracker(newNick)
    newInfo = {
        "job" : nickInfoList2[0],
        "level" : nickInfoList2[1],
        "exp" : nickInfoList2[2],
        "popularity" : nickInfoList2[3],
        "union" : union2
    }


    return

if __name__ == "__main__":
    print(tracker('창일'))