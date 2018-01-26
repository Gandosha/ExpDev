# ExpDev

* Identify the vuln port (netstat -noa on target // nmap the target).
* Attach the procces to Immunity debugger and "Play" it on the target.
* Edit Fuzzer.py (IP address, port and what it sends in the socket - Ex. SLmail's Fuzzer in repo).
* Fuzz the target.
* Identify A's in the registries (especially EIP - it controls the execution flow).
* Write a POC that relies on the fuzzer (Ex. SLmail's POC in repo).
