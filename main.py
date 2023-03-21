#!/bin/bash

def getBegining():
    with open('logFile.txt','r') as f:
        beg = []
        for line in f:
            line = line.strip()
            if line.endswith('begin'):
                sline = line.split()
                sline = sline[1]
                sline = sline.split(':')
                sline = ''.join(sline)
                beg.append(float(sline))
    return beg


def getEnding():
    with open('logFile.txt', 'r') as f:
        end = []
        for line in f:
            line = line.strip()
            if 'end' in line:
                sline2 = line.split()
                sline2 = sline2[1]
                sline2 = sline2.split(':')
                sline2 = ''.join(sline2)
                end.append(float(sline2))
    return end

def getFastestTrans():
    bg = getBegining()
    end = getEnding()
    result = 1
    original = 0
    for i in range(len(bg)):
        for k in range(len(end)):
            x = bg[i] - end[i]
            if x < result:
                result = x
                original = bg[i]
            break
    original = str(original).split('.')
    original = original[1]
    return original



def ID():
    val = getFastestTrans()
    rs = None
    with open('logFile.txt','r') as f:
        for i in f:
            i = i.strip()
            if val in i and i.endswith('begin'):
                i = i.split()
                i = i[6]
                rs = i

    return print(f"The ID of the Fastest transaction is {rs}")

ID()