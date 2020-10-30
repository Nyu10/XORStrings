import sys
import math
mode = sys.argv[1]#human or numOut
keyfile = sys.argv[2] #keyfile
inpfile = sys.argv[3]#textfile
key = open(keyfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
inp = open(inpfile).read()[:-1] #removes the mandatory \n at the end of the file to support one line messages.
debug = False

if(debug):
    print("mode:"+mode)
    print("key: "+key)
    print("inp: "+inp)


expanded_key = key*(math.floor(len(inp)/len(key))+1)

String =""

if (mode=="human"):
    for x in range(len(inp)):
        #int value of the letter in the message
        a = ord(inp[x])
        #int value of corresponding key
        #b=ord(expanded_key([x]))
        b=(ord(expanded_key[x]))
        String += chr(a^b)
if (mode=="numOut"):
    for x in range(len(inp)):
        #int value of the letter in the message
        a = ord(inp[x])
        #int value of corresponding key
        #b=ord(expanded_key([x]))
        b=(ord(expanded_key[x]))
        String += hex(a^b).lstrip("0x").rstrip("L")+ " "

print(String)