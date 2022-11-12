#############################################################################
# Team Horus
# Vigenere Cypher
# 9/23/2022
#############################################################################

import sys

# holds the user input for encrypt/decrypt and the key
crypt = sys.argv[1]
mykey = sys.argv[2].upper()
mykey = ''.join(e for e in mykey if e.isalpha()) # removes all non-alpha characters from the key

# loops until interrupted
for string in sys.stdin:

    # converts the key to a list for manipulation and traversing
    key = list(mykey)
    
    # assigns the message to be en/decoded to a variable
    plaintext = string[:-1].upper()
    ciphertext = string[:-1].upper() 

    # loops the key to the length of the message
    for i in range(len(plaintext)-len(key)):
        key.append(key[i%len(key)])

    # for encryption
    if crypt == '-e':
        ciphertext = []
        for i in range(len(plaintext)):
            
            # checks for alphabet only characters
            if plaintext[i].isalpha():
                
                # the math seen in crytography notes using ASCII
                C = (ord(plaintext[i]) + ord(key[i]))%26
                C += 97 # converts alphabet numericals to ASCII equivalent
                
                # keeps track of cases within the message
                if string[i].islower():
                    ciphertext.append(chr(C))
                else:
                    ciphertext.append(chr(C).upper())

            # keeps track of non-alpha characters
            else:
                ciphertext.append(plaintext[i])
                key.insert(i, ' ') # keeps the ith position of the key proportional to the message

        # combines and prints finished ciphertext
        ciphertext = "".join(ciphertext)
        print(ciphertext)
            
    # for decryption
    elif crypt == '-d':
        plaintext = []
        for i in range(len(ciphertext)):

            # checks for alphabet only characters
            if ciphertext[i].isalpha():

                # the math seen in crytography notes using ASCII
                P = (26 + ord(ciphertext[i]) - ord(key[i]))%26
                P += 97 # converts alphabet numericals to ASCII equivalent

                # keeps track of cases within the message
                if string[i].islower():
                    plaintext.append(chr(P))
                else:
                    plaintext.append(chr(P).upper())

            # keeps track of non-alpha characters
            else:
                plaintext.append(ciphertext[i])
                key.insert(i, ' ')

        # combines and prints finished decrypted message
        plaintext = "".join(plaintext)
        print(plaintext)
