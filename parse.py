import fileinput
import hashlib
import math
pairs = dict() #dictionary of associations
def initial_parser(lines):
    parser = getresult(lines)

def getresult(lines):
    global minimum
    i=0
    for line in lines:
        each_word = line.splitlines()[0].split(',')
        if(i==0):
            minimum=int(each_word[0])
        i=i+1
        buildDict(each_word)

def buildDict(words):
    global pairs
    for i in range(len(words)):
        for j in range(len(words)):
            if words[i] != words[j]:
                if(i<j):
                    index =   words[i]+ "+" + words[j]
                    if index not in pairs.keys() :
                        pairs[index] = 1
                    else:
                        pairs[index] = pairs[index] + 1
                else:
                    reverseIndex =  words[j]+ "+" + words[i]
                    if(reverseIndex not in pairs.keys()):
                        pairs[reverseIndex]= 1
initial_parser(fileinput.input())
for key in pairs:
    if(pairs[key] >= minimum):
        print key +":" +str(pairs[key])
pairs={}
