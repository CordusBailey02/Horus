#################################################################
# Steg                                                          #
# Team Horus                                                    #
# Names: Cordus Bailey, Casey Lee, Josue Gaona, Brianna Butler, #
#        Calin Farmer, Nathan Granade, Braylen Simmons          #
# 10/19/2022                                                    #
#################################################################
#
#   USAGE:
# python3 steg.py -(sr) -(bB) -o<val> [-i<val>] -w<val> [-h<val>]
#
#################################################################
import sys

# Stores the arguments given in the command line & the value for SENTINEL
store = False
retrieve = False
bitMode = False
byteMode = False
offset = 0
interval = 1
wrapperFile = ""
hiddenFile = ""
SENTINEL = bytearray(b'\x00\xFF\x00\x00\xFF\x00')

# Goes through the arguments and sets the corresponsing variable
# above to the value of the given argument
for arg in sys.argv:
    if(arg == "-s"):
        store = True
    elif(arg == "-r"):
        retrieve = True
    elif(arg == "-b"):
        bitMode = True
    elif(arg == "-B"):
        byteMode = True
    elif(arg[:2] == "-o"):
        offset = int(arg[2:], 10)
    elif(arg[:2] == "-i"):
        interval = int(arg[2:], 10)
    elif(arg[:2] == "-w"):
        print("WRAPPER: " + arg[2:])
        wrapperFile = arg[2:]
    elif(arg[:2] == "-h"):
        hiddenFile = arg[2:]

# Opens and reads the wrapper file as a bytearray
wrapperFile = open(wrapperFile, "rb")
wrapperFileData = bytearray(wrapperFile.read())
wrapperFile.close()


#BYTE method
if(byteMode):

    # Determines if store(-s) was selected
    if(store):

        # Opens and reads the file to hide in the wrapper as a bytearray
        file = open(hiddenFile, "rb")
        hiddenFileData = bytearray(file.read())
        file.close()

        # Puts the hidden file data into the wrapper file
        i = 0
        while(i < len(hiddenFileData)):
            wrapperFileData[offset] = hiddenFileData[i]
            offset += interval
            i += 1

        # Puts the SENTINEL value at the end to show the end of the hidden message
        i = 0
        while(i < len(SENTINEL)):
            wrapperFileData[offset] = SENTINEL[i]
            offset += interval
            i += 1

        # Outputs bytearray of wrapper file with a hidden file inside of it
        sys.stdout.buffer.write(wrapperFileData)

    # Determines if retrieve(-r) was selected instead of store(-s)
    elif(retrieve):
        # Creates a bytearray to store the hidden file data as we find it
        # And creates a bytearray(b) to hold the byte we take from the wrapper
        # file data while searching for the SENTINEL value
        hiddenFileData = bytearray()
        b = bytearray(1)
        foundSentinel = False

        # Loops through the wrapper file data and grabs a byte to come to
        # the SENTINEL value
        while(offset < len(wrapperFileData) and foundSentinel == False):
            b[0] = wrapperFileData[offset]

            # Checks if b equals a SENTINEL byte
            if(b[0] == SENTINEL[0]):
                # Creates a bytearray to hold a possible SENTINEL value
                senti = bytearray()
                senti.extend(b)
                offset += interval

                # Loops through the rest of the bytes in the file
                # and compares them to the SENTINEL bytes
                i = 1
                while(offset < len(wrapperFileData)):
                    b[0] = wrapperFileData[offset]

                    # Adds b to the possible SENTINEL value(senti)
                    # Goes to the next byte and continues the while-loop
                    if(b[0] == SENTINEL[i]):
                        senti.extend(b)
                        offset += interval
                        i += 1
                    # Adds our possible SENTINEL value(senti) to the
                    # hidden file data if a byte in b doesn't match
                    # the byte in the SENTINEL value
                    elif(b[0] != SENTINEL[i]):
                        hiddenFileData.extend(senti)
                        break

                    # Breaks out of the inner while-loop
                    # And sets 'foundSentinel' to True
                    if(senti == SENTINEL):
                        foundSentinel = True
                        break

            # Adds b to the hidden file data
            hiddenFileData.extend(b)
            offset += interval

        # Outputs bytearray of hiddenFileData to give us the hidden file
        # inside of the orignal file
        sys.stdout.buffer.write(hiddenFileData)

# BIT method
if(bitMode):

    # Determines if store(-s) was selected
    if(store):
        # Opens and reads the file to hide in the wrapper as a bytearray
        file = open(hiddenFile, "rb")
        hiddenFileData = bytearray(file.read())
        file.close()

        # Puts the hidden file data into the wrapper file
        # For loop used to go through 8 bits(1 Byte) and add them
        # to the wrapperFileData
        i = 0
        while(i < len(hiddenFileData)):
            for j in range(0, 8):
                wrapperFileData[offset] &= 0b11111110
                wrapperFileData[offset] |= ((hiddenFileData[i] & 0b10000000) >> 7)
                hiddenFileData[i] = ((hiddenFileData[i] << 1) & (2 ** 8 - 1))
                offset += interval
            i = i + 1

        # Puts the SENTINEL value into the wrapper file
        # For loop used to go through 8 bits(1 Byte) and add them
        # to the wrapperFileData
        i = 0
        while(i < len(SENTINEL)):
            for j in range(0, 8):
                wrapperFileData[offset] &= 0b11111110
                wrapperFileData[offset] |= ((SENTINEL[i] & 0b10000000) >> 7)
                SENTINEL[i] = (SENTINEL[i] << 1) & (2 ** 8 - 1)
                offset += interval
            i = i + 1


        # Outputs bytearray of wrapper file with a hidden file inside of it
        sys.stdout.buffer.write(wrapperFileData)

    # Determines if retrieve(-r) was selected instead of store(-s)
    elif(retrieve):
        # Creates a bytearray to store the hidden file data as we find it
        # And creates a bytearray(b) to hold the byte we take from the wrapper
        # file data while searching for the SENTINEL value
        hiddenFileData = bytearray()
        b = bytearray(1)
        foundSentinel = False

        # Loops through the wrapper file data and grabs a byte to come to
        # the SENTINEL value
        while(offset < len(wrapperFileData) and foundSentinel == False):
            b[0] = 0

            # Loops through 8 bits(1 Byte) to compare to a SENTINEL byte
            for j in range(0, 8):
                b[0] |= (wrapperFileData[offset] & 0b00000001)
                if(j < 7):
                    b[0] = (b[0] << 1) & (2 ** 8 - 1)
                    offset += interval

            # Checks if b equals a SENTINEL byte
            if(b[0] == SENTINEL[0]):
                # Creates a bytearray to hold a possible SENTINEL value
                senti = bytearray()
                senti.extend(b)
                offset += interval

                # Loops through the rest of the bytes in the file
                # and compares them to the SENTINEL bytes
                i = 1
                while(offset < len(wrapperFileData)):
                    b[0] = 0

                    # Loops through 8 bits(1 Byte) to compare to a SENTINEL byte
                    for j in range(0, 8):
                        b[0] |= (wrapperFileData[offset] & 0b00000001)
                        if(j < 7):
                            b[0] = (b[0] << 1) & (2 ** 8 - 1)
                            offset += interval

                    # Adds b to the possible SENTINEL value(senti)
                    # Goes to the next byte and continues the while-loop
                    if(b[0] == SENTINEL[i]):
                        senti.extend(b)
                        offset += interval
                        i += 1

                    # Adds our possible SENTINEL value(senti) to the
                    # hidden file data if a byte in b doesn't match
                    # the byte in the SENTINEL value
                    elif(b[0] != SENTINEL[i]):
                        hiddenFileData.extend(senti)
                        break

                    # Breaks out of the inner while-loop
                    # And sets 'foundSentinel' to True
                    if(senti == SENTINEL):
                        foundSentinel = True
                        break
            # Adds b to the hidden file data
            hiddenFileData.extend(b)
            offset += interval

        # Outputs bytearray of hiddenFileData to give us the hidden file
        # inside of the orignal file
        sys.stdout.buffer.write(hiddenFileData)
