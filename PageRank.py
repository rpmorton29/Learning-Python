import sys
import os.path as osp
import math



def readfile(file):
    contents = open(file, 'r')
    symbols = '''!()-[']{};:'"\,<>./?@#“““”’$%^&*_~'''
    wordDict = {}
    linenum = 0
    linelist = []
    wordcount = 0
    pageNum = 1
    for line in contents:
        linenum += 1
        if linenum % 26 == 0:
            pageNum += 1
        wordlist = line.split()
        for word in wordlist:
            word = word.lower()
            while (word[len(word) - 1] or word[0]) in symbols and len(word) > 1:

                if word[len(word) - 1] in symbols:
                    # print("true")
                    word = word[0:len(word) - 1]
                if word[0] in symbols:

                    word = word[1:len(word)]
                else:
                    break

            if len(word) >= 3:
                if word not in wordDict:
                    wordcount += 1
                    num = 1
                    wordDict[word] = [num, set(), set()]
                    wordDict[word][1].add(linenum)
                    wordDict[word][2].add(pageNum)
                else:
                    wordDict[word][0] += 1
                    wordDict[word][1].add(linenum)
                    wordDict[word][2].add(pageNum)

            # print(word.lower() )

    removeTen(wordDict,wordcount)
    totals = pagerank(wordDict)
    makeReport(totals)
    #for keys in wordDict:
        #print(wordDict[keys])


def removeTen(dict,count):
    values = []
    removenum = math.ceil(count *.10)
    #print(count-removenum)
    for words in dict:
        values.append(dict[words][0])
    while removenum>0:
        target = min(values)
        removenum = removenum - 1
        rkey = ""
        for word in dict:
            if dict[word][0] == target:
                rkey=word
        del dict[rkey]

    #print("removed", len(dict))

def pagerank(dict):
    pages= []

    keylist = getkeys()
    score = []
    for word in dict:
        pages.extend(dict[word][2])
    pagemax = max(pages)
    for pages in range(0,pagemax+1):
        single = onepage(dict,keylist,pages)
        pair = 0
        trip = 0
        four = 0

        if len(keylist)>=2:
            pair = two(dict, keylist, pages)
        if len(keylist)>=3:
            trip = threes(dict, keylist, pages)
        if len(keylist)== 4:
            four= fours(dict, keylist, pages)
        total = single+pair+trip+four
        score.append(total)
    return score

def onepage(dict, k, pg):
    points = 0

    for j in range(0, len(k)):
        info = dict.get(k[j])
        if pg in info[2]:
            points += 1
    return points
def two(dict, k, pg):
    score = 0

    for j in range(0,len(k)):
        for n in range(j+1,len(k)):
            data1 = dict.get(k[j])
            data2 = dict.get(k[n])
            if pg in data1[2] and pg in data2[2]:
                score += 2
                if data1[1].intersection(data2[1]) is not None:
                    score += 5
    return score


def threes(dict, k, pg):
    score = 0

    for j in range(0, len(k)):
        for n in range(j + 1, len(k)):
            for m in range(n+1,len(k)):
                data1 = dict.get(k[j])
                data2 = dict.get(k[n])
                data3 = dict.get(k[m])
                if pg in data1[2] and pg in data2[2] and pg in data3[2]:
                    score += 3
                    
                    if data1[1].intersection(data2[1]).intersection(data3[1]) is not None:
                        score += 6
    return score
def fours(dict, k, pg):
    score = 0


    data1 = dict.get(k[0])
    data2 = dict.get(k[1])
    data3 = dict.get(k[2])
    data4 = dict.get(k[3])
    if pg in data1[2] and pg in data2[2] and pg in data3[2] and pg in data4[2]:
        score += 3
        if data1[1].intersection(data2[1]).intersection(data3[1]).intersection(data4[1]) is not None:
            score += 6
    return score

def getkeys():
    keys = []
    if len(sys.argv) == 3:
        keys.append(sys.argv[2])
    elif len(sys.argv) == 4:
        for i in range(2,4):
            keys.append(sys.argv[i])
    elif len(sys.argv) == 5:
        for i in range(2,5):
            keys.append(sys.argv[i])
            #print(sys.argv[i])
    elif len(sys.argv) == 6:
        for i in range(2,6):
            keys.append((sys.argv[i]))
            #print(sys.argv[i])
    #print(keys)
    return keys

def makeReport(scores):
    top = scores.index(max(scores))
    top = scores.index(max(scores))
    print("top page", top, scores[top])
    for i in range(1,11):
        next= scores.index(max(scores))
        print(i,".   ", next , "\t", max(scores))
        scores[next] = -1






if len(sys.argv) == 1:
    print("Please supply more arguments.")
elif len(sys.argv) > 6:
    print(len(sys.argv))
    print(sys.argv[:])
else:
    filename = sys.argv[1]


    if not osp.exists(filename):
        print("The file ", filename, "does not exist. Try again.")
    elif not osp.isfile(filename):
        print("The name ", filename, "is not a file. Try again.")
    else:
        try:
            this = open(filename)
        except PermissionError:
            print("You do not have permission to access the directory ", filename)
            sys.exit()
    readfile(filename)


