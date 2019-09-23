import requests
from bs4 import BeautifulSoup

url = 'http://www.ankitfadia.in'  # website of a hacker offering hacking courses
head = {'User-Agent': 'Chrome/50.0.2661.102'}
req = requests.get(url, headers=head)

soup = BeautifulSoup(req.text, "html.parser")

bullets = soup.find('div', class_='modal-body').find_all('li')  # getting the topic names in syllabus

points = [x.text for x in bullets]

print(*points, sep="\n")

''' 
Introduction to Ethical Hacking
IP Addresses
IP Enumeration and  Tracing
IP Hiding and Bypassing Restrictions
Proxy Servers, VPNs and Proxy Bouncers
HTTP Tunnelling, Unblocking Websites and People Hacking
Network Reconnaissance & Information Gathering
Metasploit
Spoofing Attacks, Google Dorking and Website Enumeration.
Trojans, Keyloggers and Spyware Attacks
Mobile Phone Exploits
Password Cracking Attacks
Windows Vulnerabilities
Data Encryption, Data Hiding and Steganography
DOS Attacks
Distributed DOS Attacks
Web Attacks
Cookie Stealing and Session Hijacking
Phishing Attacks
Open Redirection Attacks
Cross Site Scripting Attacks
Data Sniffing
ARP Poisoning
SQL Injection
Advanced SQL Injection
25 Attacks with Backtrack / Kali
Meterpreter & Post Exploitation Attacks
Advanced Meterpreter & Post Exploitation Attacks
Post Exploitation Scripts and Modules
Shell Attacks
Bind Shell Attacks
Reverse Shell Attacks
Wi-Fi Cracking
WEP Cracking
WPA Cracking
WPA2 Cracking
Computer Forensics & Honeypots
Social Engineering Toolkit Attacks
Kali Hacking
Advanced Kali Hacking
Project Work for Hands-On Experience

'''
