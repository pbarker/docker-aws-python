from config import config
import urllib.request

'''
Created on Apr 17, 2015
@author: Grillz
'''

def getAAlias():
    return config.getConfig('aName')

def getCAlias():
    data = config.getFullConfig()
    c = config.getConfig('cScheme')
    for (key, value) in data.items():
        if key in c:
            c = c.replace(key, value)
    return c

def getPublicIp():
    with urllib.request.urlopen('http://ip.42.pl/raw') as response:
        ip = response.read()
        return ip
