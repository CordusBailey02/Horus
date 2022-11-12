#############################################################################################################
# Team Horus
# Names: Cordus Bailey, Casey Lee, Josue Gaona, Brianna Butler, Calin Farmer, Nathan Granade, Braylen Simmons
# MODIFIED TimeLock Program: Adds middle letter in hash to the end
# 10/28/2022
##############################################################################################################

####################################################################################
# HOW TO RUN IN LINUX CMD LINE
#
# cd [path holding timelock.py]
#
# python3 timelock.py < epoch.txt 
# (epoch.txt containing only date in YYYY MM DD HH mm SS format)
#
# OR
#
# echo "YYYY MM DD HH mm SS" | python3 timelock.py
####################################################################################

import sys, time
from datetime import datetime, timedelta
import hashlib
import math

# splits the stdin for formatting
for line in sys.stdin:
    epoch = line.split()

# assigns date elements to variables
YYYY = int(epoch[0])
MM = int(epoch[1])
DD = int(epoch[2])
HH = int(epoch[3])
mm = int(epoch[4])
SS = int(epoch[5])

# creates the datetime objects for the epoch and current times
epochTime = (datetime(YYYY, MM, DD, HH, mm, SS))
currentTime = datetime.now()

# TO TEST: Replace variables with respective date (remove any leading zeros)
# currentTime = datetime(YYYY, MM, DD, HH, mm, SS)

# eliminates time differences with daylight savings time
if time.localtime(time.mktime(epochTime.timetuple())).tm_isdst:
    epochTime -= timedelta(hours=1)

if time.localtime(time.mktime(currentTime.timetuple())).tm_isdst:
    currentTime -= timedelta(hours=1)

# gets the difference in seconds as a non-floating integer
seconds = math.floor((currentTime - epochTime).total_seconds())
extra = math.floor(seconds%60)
totalSeconds = str(seconds-extra)

# computes MD5(MD5(time elapsed)) to get the compound hash
hashstring = (hashlib.md5((hashlib.md5(totalSeconds.encode()).hexdigest()).encode())).hexdigest()

# creates variables for the TimeLock "code"
hashcodeAlpha = ""
hashcodeDigit = ""
hashcode = ""

# gets the first two letters in the compound hash
for i in range(len(hashstring)):
    if hashstring[i].isalpha():
        hashcodeAlpha += hashstring[i]
    if len(hashcodeAlpha) > 1:
        break

middleHashl = ""
# gets the last two numbers (from right to left) in the compound hash
for j in range(1, len(hashstring)):
    if hashstring[-j].isdigit():
        hashcodeDigit += hashstring[-j]
    if len(hashcodeDigit) > 1:
        break

# Gets the middle of the hash and adds it to the end
for k in range(len(hashstring)):
    if(k == len(hashstring)/2):
        middleHashl = hashstring[k]
    

# completes the TimeLock code and sends to stdout
hashcode = hashcodeAlpha + hashcodeDigit
print(hashcode + middleHashl)
        










