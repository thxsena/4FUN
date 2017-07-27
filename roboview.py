#!/usr/bin/env python
# -*- coding: utf-8 -*- 
# 
# Author: Thiago Sena a.k.a THX 
# Ctf Team: Fireshell
# Github: github.com/thxsena
# 
#

import requests
import time
import sys



def prRed(prt): print("\033[91m {}\033[00m" .format(prt))

prRed("""

 ██▀███   ▒█████   ▄▄▄▄    ▒█████   ██▒   █▓ ██▓▓█████  █     █░ 
▓██ ▒ ██▒▒██▒  ██▒▓█████▄ ▒██▒  ██▒▓██░   █▒▓██▒▓█   ▀ ▓█░ █ ░█░ 
▓██ ░▄█ ▒▒██░  ██▒▒██▒ ▄██▒██░  ██▒ ▓██  █▒░▒██▒▒███   ▒█░ █ ░█  
▒██▀▀█▄  ▒██   ██░▒██░█▀  ▒██   ██░  ▒██ █░░░██░▒▓█  ▄ ░█░ █ ░█ 
░██▓ ▒██▒░ ████▓▒░░▓█  ▀█▓░ ████▓▒░   ▒▀█░  ░██░░▒████▒░░██▒██▓  v1.0
░ ▒▓ ░▒▓░░ ▒░▒░▒░ ░▒▓███▀▒░ ▒░▒░▒░    ░ ▐░  ░▓  ░░ ▒░ ░░ ▓░▒ ▒   
  ░▒ ░ ▒░  ░ ▒ ▒░ ▒░▒   ░   ░ ▒ ▒░    ░ ░░   ▒ ░ ░ ░  ░  ▒ ░ ░  
  ░░   ░ ░ ░ ░ ▒   ░    ░ ░ ░ ░ ▒       ░░   ▒ ░   ░     ░   ░  
   ░         ░ ░   ░          ░ ░        ░   ░     ░  ░    ░    
                        ░               ░                     

""")


site = raw_input("[*] Site: ")
print ""
print "[*]Checking Status..."
time.sleep(2)

print '-'*60

r = requests.get(site)
print '[*]Status:', r.status_code
print '-'*60

if r.status_code == 200:
	print "[*]Ok"
else:
	print "[*]Down"
	sys.exit()

print '-'*60

time.sleep( 2 )

print "[*]Robots..."
print ""

time.sleep( 2 )

session = requests.Session()
hearders={'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36'}
r = requests.get(site +'/robots.txt')

if r.status_code == 404:
	print"[*]Not fund"
else:
	print r.text

	sys.exit()
