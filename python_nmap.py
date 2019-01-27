#!/usr/bin/python3

import nmap

scanner = nmap.PortScanner()

print("------------------Welcome to the H1mSR0cK nmap Scanner--------------------------")
print("--------------------------------------------------------------------------------")
print("------------------Enter the Ip address to scan----------------------------------")

ip_input = input()

print("------------------Enter the number of particular scan---------------------------")
print("""\n press
	 (1)SYN ACK Scan
	 (2)UDP Scan
	 (3)Comprehensive Scan \n""")

scan_type = int(input())

print("------------------nmap scanner version------------------------------------------")
print("nmap scanner version",scanner.nmap_version())

if scan_type == 1:
	scanner.scan(ip_input,'1-1024','-v -sS')
	print(scanner.scaninfo())
	print(scanner[ip_input].all_protocols())
	print("open ports:",scanner[ip_input]['tcp'].keys())

elif scan_type == 2:
	scanner.scan(ip_input,'1-1024','-v -sU')
	print(scanner.scaninfo())
	print(scanner[ip_input].all_protocols())
	print("open ports:",scanner[ip_input]['udp'].keys())

elif scan_type == 3:
	scanner.scan(ip_input,'1-1024','-v -sS -sV -sC -A -O')
	print(scanner.scaninfo())
	print(scanner[ip_input].all_protocols())
	print("open ports:",scanner[ip_input]['tcp'].keys())

else:
	print("wrong choice")

print("----------------------Thank you!-----------------------------------------------")


