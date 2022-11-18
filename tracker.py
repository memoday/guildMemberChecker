import checkInfo as ci

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
            if int(trackingNickInfo["popularity"])-30 <= int(newNickInfo["popularity"]) <= int(trackingNickInfo["popularity"])+100:
                if trackingNickInfo['union'] == '0':
                    if int(trackingNickInfo["popularity"])-10 <= int(newNickInfo["popularity"]) <= int(trackingNickInfo["popularity"])+50:
                        check = 'true'
                elif int(trackingNickInfo["union"])-100 <= int(newNickInfo["union"]) <= int(trackingNickInfo["union"])+250:
                    check = 'true'
    else:
        check = 'false'

    return check