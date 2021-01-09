from bit import *
from bit.format import bytes_to_wif
from random import *


print('What challenge shall we beat?')
challengeint = input()
challengeint = int(challengeint)
addressfile = open("addresslist.txt", "r")
challenge = addressfile.readlines()
challengeaddress = challenge[challengeint -1]
challengeaddress = challengeaddress.strip()
print('Challenge Address: ',challenge[challengeint -1])
addressfile.close()

maxfile = open("maxlist.txt", "r")
maxlimit = maxfile.readlines()
maxilimit = int(maxlimit[challengeint -1])
print('Range Upper Limit: ',maxlimit[challengeint -1])
maxfile.close()

pkey = 0
plus1 = 1
totalscantime = 0
scantime = 0

hunt = challengeaddress
print('CHALLENGE ACCEPTED')
print('searching.........')

while True:
    scantime +=1
    pkey= randint(1,maxilimit)
    hexpkey = hex(pkey)
    hexpkey = hexpkey [2:]
    prvstring = hexpkey
    prvstring = str(prvstring)
    prvstring = prvstring.zfill(64)
    key = Key.from_hex(prvstring)
    pubaddresscomp = str(key.address)    
    
    if pubaddresscomp == hunt:
        print(pubaddresscomp)
        data = open("btclist.txt", "w")
        print (prvstring,file = data)
        print (pubaddresscomp, file = data)
        data.close()
        break
    
    if scantime == 100000:
        totalscantime = totalscantime + scantime
        scantime = 0
        print(totalscantime,'keys searched')
    
print("Bitcoin Found")
print(pubaddresscomp)
print(prvstring)
print(totalscantime)
status = open("nohupstatus.txt","a")
print("coin found closed",file = status)
status.close()
