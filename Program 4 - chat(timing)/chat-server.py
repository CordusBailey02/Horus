import socket
import time

ZERO = 0.02
ONE = 0.08

try:
    
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    port = 1337
    s.bind(("", port))
    s.listen(0)
except:
    print("Error")

covert = "secret" + "EOF"
covert_bin = ""
for i in covert:
    covert_bin += bin(ord(i))[2:].zfill(8)
    #print(i, "->", ord(i), "->", bin(ord(i))[2:].zfill(8))
    #covert_bin += bin(int(hexlify(i), 16))[2:].zfill(8)

c, addr = s.accept()
msg = "Some message..."

n = 0
for j in range(len(covert)):
    for i in msg:
        c.send(i.encode())
        #time.sleep(0.025)
        if(covert_bin[n] == "0"):
            time.sleep(ZERO)
        else:
            time.sleep(ONE)
        n = (n + 1) % len(covert_bin)
        
c.send("EOF".encode())
c.close()
