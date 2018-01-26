# ExpDev

* Identify the vuln port (netstat -noa on target // nmap the target).
* Attach the procces to Immunity debugger and "Play" it on the target.
* Edit Fuzzer.py (IP address, port and what it sends in the socket - Ex. sLmail_pop3_pass_fuzzer.py in repo).
* Fuzz the target.
* Write a POC that replicates the crash (Ex. slmail_pop3_replicated_crash.py in repo).
* Locate those 4 A's that overwrite the EIP register.
* Send a unique string in order to identify the EIP offset. The size of this string is equal to the amount of bytes that crash the service. Use pattern_create in kali (Ex. pattern_create.rb -l 2700 --> place the output in buffer variable. See  	slmail_pop3_pattern_create.py in repo).
* Use pattern_offset.rb to discover the offset of these specific 4 bytes in the unique byte string and edit buffer variable (Ex. pattern_offset.rb -l 2700 -q 39694438. See slmail_pop3_pattern_offset.py
in repo).
* Locate space for the shellcode - a standart reverse shell payload requires about 350-400 bytes of space. Locate a convenient location to place the shellcode using the crash in Immunity debugger (Ex. C's in slmail crash are 90 bytes. You can increase the buffer length in order to make the shellcode fit. Ex. Increased buffer in slmail from 2700 to 3500. See slmail_pop3_locate_space.py in repo).
* Check for bad characters - an easy way to do this is to send all possible chars, from 0x00 to 0xff, as part of the buffer variable. See how these chars are dealt with by the app in memory dump of ESP register (Follow in dump - 01 02 03 etc..), after the crash (Ex. 0x00 - null byte is always bad. See slmail_pop3_bad_chars.py).
* Run the badchars check again and again till it doesnt trancate the values in memory (delete the relevnt chars before running the check in buffer, of course).
