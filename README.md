# ExpDev

* Identify the vuln port (netstat -noa on target // nmap the target).
* Attach the procces to Immunity debugger and "Play" it on the target.
* Edit Fuzzer.py (IP address, port and what it sends in the socket - Ex. sLmail_pop3_pass_fuzzer.py in repo).
* Fuzz the target.
* Write a POC that replicates the crash (Ex. slmail_pop3_replicated_crash.py in repo).
* Locate those 4 A's that overwrite the EIP register.
* Send a unique string in order to identify the EIP offset. The size of this string is equal to the amount of bytes that crash the service. Use pattern_create in kali (Ex. pattern_create.rb -l 2700 --> place the output in buffer variable. See  	slmail_pop3_pattern_create.py in repo).
* Use pattern_offset.rb to discover the offset of these specific 4 bytes in the unique byte string and edit buffer variable (Ex. pattern_offset.rb -l 2700 -q 39694438).
