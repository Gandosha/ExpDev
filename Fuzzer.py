#!/usr/bin/python
import socket

buffer = ["A"]
counter = 50

while len(buffer) <= 1000:
    buffer.append("A" * counter)
    counter = counter + 50

for buffstring in buffer:
    print "Fuzzing:" + str(len(buffstring))
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.connect( ("<IP_ADDRESS_TO_FUZZ>", <PORT_TO_FUZZ>) )
    sock.send(buffstring)
    sock.close()
