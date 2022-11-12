#################################################################
# Chat (timing) Covert Channel                                  #
# Team Horus                                                    #
# Names: Cordus Bailey, Casey Lee, Josue Gaona, Brianna Butler, #
#        Calin Farmer, Nathan Granade, Braylen Simmons         #                                             
# 10/13/22                                                      #
#################################################################
#                                                               #
#   USAGE(RUN IN THE TEMRINAL):                                 #
#   python3 chat-client.py                                      #
#                                                               #
#################################################################
import socket
import sys
from time import time

# Time used to compare to delta
TIME = 0.08

# DEBUG mode prints the time between each data being receieved
DEBUG = True

# The IP address and port to connect to
IP = "localhost"
PORT = 1337

# Connects to the server using the IP and PORT above
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((IP, PORT))

# Holds the binary string we create from the timings
covert_bin = ""
# Gets the data being transmitted
data = s.recv(4096)

# Checks to see if the data it recieved ended in 'EOF'
while((data.decode()).rstrip("\n") != "EOF"):
    sys.stdout.write(data.decode())
    sys.stdout.flush()

    # Times how long it takes to recieve the data
    t0 = time()
    data = s.recv(4096)
    t1 = time()

    # Rounds the time we got to 3 decimal places
    delta = round(t1 - t0, 3)

    # When DEBUG is set to 'True' this prints the time calculated above
    if(DEBUG == True):
        print(" DELTA: " + str(delta))

    # Determines to add either a 1 or 0 to the 'covert_bin' base on delta
    # TIME variable is set at the top of the file
    if(delta >= TIME):
        covert_bin += "1"
    else:
        covert_bin += "0"

# Stores the covert message as we create it
covert = ""
# Index of the 'covert_bin' we are at to covert it to ASCII
i = 0
# Checks to make sure the index we are at isn't larger than the string
while(i < len(covert_bin)):
    # Takes 8-bit binary of the 'covert_bin' string and saves it to binaryLetter
    # Converts the 8 -bit binary and converts it into its integer value
    binaryLetter = covert_bin[i:i + 8]
    intBinaryLetter = int(binaryLetter, 2)

    # Adds the corresponding ASCII value from intBinaryLetter to 'covert' string
    # Adds a '?' to the 'covert' string when an error occurs
    try:
        covert += chr(intBinaryLetter)
    except TypeError:
        covert += "?"

    # Checks to see if the covert string contains 'EOF'
    # If yes, it breaks the while loop(ends collecting data),
    # and removes 'EOF' from the end of the string
    if(covert[-3:] == "EOF"):
        covert = covert[:len(covert)-3]
        break

    # Increments the index by 8 to get 8-bits at a time from 'covert_bin'
    i += 8

# Disconnects from the server
s.close()

# Prints the covert message decoded from the overt message from the server
print("\nCovert Message: " + covert)
