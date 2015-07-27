from config import config
import urllib2
'''
Created on Apr 17, 2015
@author: BrickRoad
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
    ip = urllib2.urlopen('http://ip.42.pl/raw').read()
    return ip
