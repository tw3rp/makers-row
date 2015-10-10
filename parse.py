import fileinput
import math
import operator
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
    if(i<2): 
        print "error: very few lines"
    else:    
        print_output(pairs)

def sort_final_and_print(toPrint):
    sorted_pairs = sorted(toPrint.items(), key=operator.itemgetter(0))
    for i in range(len(sorted_pairs)):
        final=[sorted_pairs[i][0].split("+")[0],sorted_pairs[i][0].split("+")[1]]
        final.sort()
        print final[0] +"," + final[1]

def print_output(pairs):
    toFilter = dict() 
    toFilter = {k:v for (k,v) in pairs.iteritems() if v >= 3} 
    sort_final_and_print(toFilter)

def buildDict(words):
    global pairs
    words.sort()
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
