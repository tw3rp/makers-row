import fileinput
def parser():
    i=0
    for line in fileinput.input():
        input_line = line.splitlines()[0].split(',')
        if i==0:
            number = input_line
        else:
            print input_line[0]
        i=i+1
    print int(number[0])

parser()
