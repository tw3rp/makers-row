import fileinput
import hashlib
def parser():
    i=0
    word_prev=''
    for line in fileinput.input():
        # for j in range(len(line.splitlines()[0].split(','))):
        input_line = line.splitlines()[0].split(',')
        for word in input_line:
            if i==0:
                number = input_line
            else:
                hashid = hashlib.md5((word).encode('utf-8'))
                print word+","+word_prev
                word_prev=word
                # print "word number: "+ str(j) +",word: " + input_line[j]
        i=i+1
    #print int(number[0])

parser()
