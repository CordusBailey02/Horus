#################################################################
# Binary Decoder                                                #
# Team Horus                                                    #
# Names: Cordus Bailey, Casey Lee, Josue Gaona, Brianna Butler, #
#        Calin Farmer, Nathtan Granade, Braylen Simmons         #                                             
# 9/30/2022                                                     #
#################################################################
# use Python 3  
from ftplib import FTP

# FTP server details
IP = "138.47.134.55"
PORT = 21
USER = "anonymous"
PASSWORD = ""
FOLDER = "/"  # CHANGE TO /10/ TO USE FOR 10-BIT EXAMPLE OUTPUT
USE_PASSIVE = True # set to False if the connection times out
METHOD = 7

# connect and login to the FTP server
ftp = FTP()
ftp.connect(IP, PORT)
ftp.login(USER, PASSWORD)
ftp.set_pasv(USE_PASSIVE)

# navigate to the specified directory and list files
ftp.cwd(FOLDER)
files = []
ftp.dir(files.append)

# exit the FTP server
ftp.quit()

fullBinary = ""
binary = ""
# display the folder contents
for f in files:
        perms = f[:10]
        usedPerms = ""

        if(f[:3] == "---" and METHOD == 7):
                usedPerms = f[3:10]
                for i in usedPerms:
                        if(i == "-"):
                                binary = binary + "0"
                        else:
                                binary = binary + "1"
                fullBinary = fullBinary + binary
                binary = ""
        elif(METHOD == 10):
                for i in perms:
                        if(i == "-"):
                                binary = binary + "0"
                        else:
                                binary = binary + "1"
                fullBinary = fullBinary + binary
                binary = ""

#print("BINARY FULL: " + fullBinary)
message = ""
start = 0
end = 7
for i in range(len(fullBinary)//7):
        bina = fullBinary[start:end]
        uni = int(bina, 2)
        message += chr(uni)

        start = start + 7
        end = end + 7

#print(message)
sys.stdout.write(message)


                                
