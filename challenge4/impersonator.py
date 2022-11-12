#################################################################
# Typecast Impersonator                                         #
# Team Horus                                                    #
# Names: Cordus Bailey, Casey Lee, Josue Gaona, Brianna Butler, #
#        Calin Farmer, Nathan Granade, Braylen Simmons          #                     
# 10/21/2022                                                    #
#################################################################
#                                                               #
#   USAGE:                                                      #
#   python3 impersonator.py < (typing profile file)             #
#   e.g.: pythton3 impersonator.py < profile1.txt               #
#                                                               #
#################################################################
from pynput.keyboard import Controller
from time import sleep
from random import uniform
from termios import tcflush, TCIFLUSH
from sys import stdout

# Gets the input from the given file
password = input()
timings = input()

print("Features = {}".format(password))
print("Timings = {}".format(timings))

# Gets the given password from the input
password = password.split(",")
password = password[:len(password) // 2 + 1]
password = "".join(password)

print("Sample = {}".format(password))

# Gets the key hold times and time intervals from the input
timings = timings.split(",")
timings = [ float(a) for a in timings]
keypress = timings[:len(timings) // 2 + 1]
keyinterval = timings[len(timings) // 2 + 1:]

print("KHTs = {}".format(keypress))
print("KITs = {}".format(keyinterval))

keyboard = Controller()

# Waits 5 seconds to allow time to focus on correct window
sleep(5)

i = 0
for char in password:
    # Press the key of the character in password
    keyboard.press(char)
    # Holds the key for time corresponding in keypress(key hold times)
    sleep(keypress[i])
    # Releases the pressed key after the key hold time elaspes
    keyboard.release(char)
    # Waits the time interval between each key press
    # If statement prevents index out of bounds error by
    # not using the invertval wait time after the last key is pressed
    if i != len(keyinterval):
        sleep(keyinterval[i])
        
    i = i + 1
