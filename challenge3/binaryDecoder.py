#################################################################
# Binary Decoder                                                #
# Team Horus                                                    #
# Names: Cordus Bailey, Casey Lee, Josue Gaona, Brianna Butler, #
#        Calin Farmer, Nathtan Granade, Braylen Simmons         #                                             
# 9/23/2022                                                     #
#################################################################

import sys

#gets the input from the user
inputBinary = sys.stdin.read()

#Checks to see is the binary string is divisble by 7
if((len(inputBinary) - 1) % 7 == 0):
    #string of binary numbers seperated into 7 bit strings
    ascii7Binary = ""
    #indices of the start and end of the 7 bit strings
    start = 0
    end = 7
    #loops through the inputBinary string and seperates it into 7 bit strings
    for x in range(len(inputBinary)//7):
        ascii7Binary = ascii7Binary + inputBinary[start:end] + " "
        start = start + 7
        end = end + 7

    #holds the output
    output = ""
    #turns the string of 7 bit strings into an array of the words
    #seperated using the " " that were added in the above for loop
    binarySplit = ascii7Binary.split()
    #gets the decimal value of each 7 bit binary string then converts it
    #to its ASCII value
    for y in binarySplit:
        num = int(y, 2)
        output = output + chr(num)

    #outputs the decoded message to console
    sys.stdout.write(output+"\n")

#Checks to see is the binary string is divisble by 8
elif((len(inputBinary) - 1) % 8 == 0):
    #string of binary numbers seperated into 7 bit strings
    ascii8Binary = ""
    #indices of the start and end of the 7 bit strings
    start = 0
    end = 8
    #loops through the inputBinary string and seperates it into 7 bit strings
    for x in range(len(inputBinary)//8):
        ascii8Binary = ascii8Binary + inputBinary[start:end] + " "
        start = start + 8
        end = end + 8
        
    #holds the output
    output = ""
    #turns the string of 8 bit strings into an array of the words
    #seperated using the " " that were added in the above for loop
    binarySplit = ascii8Binary.split()
    #gets the decimal value of each 8 bit binary string then converts it
    #to its ASCII value
    for y in binarySplit:
        num = int(y, 2)
        output = output + chr(num)

    #outputs the decoded message to consol
    sys.stdout.write(output+"\n")
