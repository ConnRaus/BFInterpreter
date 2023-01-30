#brainf*** interpreter

import sys

def helpMe():
    print("Usage:\npython bfinterpreter.py <bf file>")

try:
    bfcode = str(sys.argv[1])
except IndexError:
    helpMe()
    quit()

tape = [0] * 64
file = sys.argv[1]
bfcode = ""
head = 0
codeindex = 0

def readInput(file):
    textfile = open(file)
    bfcode = textfile.read()
    textfile.close()
    return bfcode

def charAt(index):
    return bfcode[index:index+1]

def interpretChar(char):
    global head
    global codeindex
    if char == '+':
        if tape[head]+1 > 255:
            tape[head] = 0
        else:
            tape[head] += 1
    if char == '-':
        if tape[head]-1 < 0:
            tape[head] = 255
        else:
            tape[head] -= 1
    if char == '.':
        if tape[head] > 127:
            print(chr(tape[head]-128), end="")
        else:
            print(chr(tape[head]), end="")
    if char == ',':
        x = input('')
        tape[head] = ord(x)
    if char == '>':
        head += 1
    if char == '<':
        head -= 1
    if char == ']':
        #if tape is 0, do nothing
        #if not zero, move codeindex back to last [
        if tape[head] != 0:
            while bfcode[codeindex:codeindex+1] != '[':
                codeindex -= 1

def runProgram(bfcode):
    global codeindex
    while codeindex < len(bfcode):
        interpretChar(charAt(codeindex))
        codeindex += 1

bfcode = readInput(file)
runProgram(bfcode)
# print(tape)