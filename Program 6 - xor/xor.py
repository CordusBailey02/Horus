#################################################################
# XOR Crypto                                                    #
# Team Horus                                                    #
# Names: Cordus Bailey, Casey Lee, Josue Gaona, Brianna Butler, #
#        Calin Farmer, Nathan Granade, Braylen Simmons          #                                             
# 10/17/2022                                                    #
#################################################################
#                                                               #
#   USAGE(RUN IN THE TEMRINAL):                                 #
#   python3 xor.py < (cipherText/plainText) [> [outputFile]]    #
#   e.g.: python3 xor.py < ciphertext > output                  #
#                                                               #
#################################################################
import sys

# Gets the file data from the file given in the command line
userInput = sys.stdin.buffer.read()

# Opens and reads the 'key' file in the same directory
keyFile = open("key", "rb")
key = keyFile.read()
keyFile.close()

# Stores the output bytearray to print
output = bytearray()

# Combines the two bytearrays into a tuple and XOR's each together
# and then appends the value to the 'output' bytearray
for x, y in zip(userInput, key):
    output.append(x ^ y)

# Sends the 'output' to either a defined file or the terminal by default
sys.stdout.buffer.write(output)
