#!/usr/bin/env python
#-*- coding: utf-8 -*-
#
# Author: Thiago(THX)
# github: github.com/thxsena 
#


import hashlib
import sys

def prRed(prt): print("\033[91m {}\033[00m" .format(prt))

prRed('''

 _____ ___________ _____  _____ _   _   ___ 
/  __ \  _  |  _  \____ |/  ___| | | | /   |
| /  \/ |/' | | | |   / /\ `--.| |_| |/ /| |
| |   |  /| | | | |   \ \ `--. \  _  / /_| |
| \__/\ |_/ / |/ /.___/ //\__/ / | | \___  |
 \____/\___/|___/ \____/ \____/\_| |_/   |_/
	    Author: Thiago (THX)

	[1] SHA1  [2] SHA224 [3] SHA256
	    [4] SHA384   [5] SHA512
		   [0] EXIT
''')



mensagem = int(input("Number: "))

def by():
	if mensagem == 0:
		sys.exit()
by()

def sha1():
	if mensagem == 1:
		aa = raw_input('Strings :')
		sha = hashlib.sha1(aa)
		sha1 = sha.hexdigest ()
		print""
		print 'SHA1: ' + sha1
		print""
sha1()

def sha224():
	if mensagem == 2:
		ab = raw_input('Strings: ')
		sha = hashlib.sha224(ab)
		sha224 = sha.hexdigest ()
		print ""
		print 'SHA224: ' + sha224
		print ""
sha224()

def sha256():
	if mensagem == 3:
		ac = raw_input('Strings: ')
		sha = hashlib.sha256(ac)
		sha256 = sha.hexdigest ()
		print""
		print 'SHA256: ' + sha256
		print""
sha256()

def sha384():
	if mensagem == 4:
		ad = raw_input('Strings: ')
		sha = hashlib.sha384(ad)
		sha384 = sha.hexdigest ()
		print""
		print 'SHA384: ' + sha384
		print""
sha384()

def sha512():
	if mensagem == 5:
		ae = raw_input('Strings: ')
		sha = hashlib.sha512(ae)
		sha512 = sha.hexdigest ()
		print ""
		print 'SHA512: ' + sha512
		print""
sha512()

