# ExpDev

* Identify the vuln port (netstat -noa on target // nmap the target).
* Attach the procces to Immunity debugger and "Play" it on the target.
* Edit Fuzzer.py (IP address, port and what it sends in the socket - Ex. SLmail_pop3_pass_fuzzer.py in repo).
* Fuzz the target.
* Identify A's in the registries (especially EIP - it controls the execution flow).
* Write a POC that replicates the crash (Ex. slmail_pop3_replicated_crash.py in repo).
