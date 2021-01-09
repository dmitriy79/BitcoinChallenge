from bit import Key
from random import randint
import sys
import time 

challengearg = sys.argv[1]
challengeint = int(challengearg)
print('Challenge Number = ', challengeint)
addressfile = open("addresslist.txt", "r")
challenge = addressfile.readlines()
challengeaddress = challenge[challengeint - 1]
challengeaddress = challengeaddress.strip()
print('Challenge Address: ', challenge[challengeint - 1])
addressfile.close()

maxfile = open("maxlist.txt", "r")
maxlimit = maxfile.readlines()
maxilimit = int(maxlimit[challengeint - 1])
lowlimit = int(maxlimit[challengeint - 2])
print('Range Lower Limit: ', lowlimit)
print('Range Upper Limit: ', maxilimit)
maxfile.close()

pkey = 0
plus1 = 1
totalscantime = 0
scantime = 0

hunt = challengeaddress
print('CHALLENGE ACCEPTED')
print('searching.........')

while True:
    if scantime == 0:
        starttime = time.time()
    scantime = scantime + plus1
    pkey = randint(lowlimit, maxilimit)
    hexpkey = hex(pkey)
    hexpkey = hexpkey[2:]
    prvstring = hexpkey
    prvstring = str(prvstring)
    prvstring = prvstring.zfill(64)
    key = Key.from_hex(prvstring)
    pubaddresscomp = str(key.address) 
    endtime = time.time() - starttime 
    
    if pubaddresscomp == hunt:
        print(pubaddresscomp)
        data = open("btclist.txt", "w")
        print(prvstring, file=data)
        print(pubaddresscomp, file=data)
        data.close()
        break
    
    if endtime == 60:
        print(scantime, 'keys per minute')
        totalscantime = totalscantime + scantime
        print(totalscantime, 'keys searched')
        scantime = 0

print("Bitcoin Found")
print(pubaddresscomp)
print(prvstring)
print(totalscantime)
status = open("nohupstatus.txt", "a")
print("coin found closed", file=status)
status.close()

