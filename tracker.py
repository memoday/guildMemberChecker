import checkInfo as ci
import requests
from bs4 import BeautifulSoup
import time

def tracker(trackNick, newNickList):

    global trackingNickInfo

    maybe = [] #닉변 유력 후보


    print(trackNick)
    nickInfoList = ci.checkAllGG(trackNick) #[닉변] 데이터셋 추가
    print(nickInfoList)
    trackingNickInfo = {
        "job" : nickInfoList[0],
        "level" : nickInfoList[1],
        "popularity" : nickInfoList[2],
        "union" : nickInfoList[3],
    }

    for i in range(len(newNickList)):
            check = compare(newNickList[i])    
            if check == 'true':
                maybe.append(newNickList[i])

    return maybe

def compare(newNick):

    nickInfoList2 = ci.checkAllGG(newNick)
    newNickInfo = {
            "job" : nickInfoList2[0],
            "level" : nickInfoList2[1],
            "popularity" : nickInfoList2[2],
            "union" : nickInfoList2[3],
        }

    check = 'false'
    

    if trackingNickInfo["job"] == newNickInfo["job"]:
        if int(trackingNickInfo["level"]) <= int(newNickInfo["level"]):
            if int(trackingNickInfo["popularity"])-30 <= int(newNickInfo["popularity"]) <= int(trackingNickInfo["popularity"])+50:
                if int(trackingNickInfo["union"])-100 <= int(newNickInfo["union"]) <= int(trackingNickInfo["union"])+250:
                    check = 'true'
    else:
        check = 'false'

    return check

if __name__ == "__main__":
    trackNick = '요담님'
    newList = ['아까마', '요담', '김재범', '단하참', '밍츄얌', '월꽁', '꺼폐', '얼음용', '펭고쿠', '너와의첫여행', '정령랜드', '꼬맹미래', '별의기도', '라린이', '김담우', '김합정', '업엽', '용콴', '성갈', 'Darkslayan', '짓버']

    print(*tracker(trackNick,newList))

    # for i in range(len(trackList)):
    #     changed_to = tracker(trackList[i],newList)
    #     if len(changed_to) > 0:
    #         print('[닉변]', str(trackList[i]),' -> ',*changed_to)
    #         changed = ('[닉변]', str(trackList[i]),' -> ',*changed_to)
    #         print('changed: ',changed)

    #     else:
    #         print('[삭제]', str(trackList[i]))
    #         changed = '[삭제]', str(trackList[i])
    #         print('changed: ',changed)
