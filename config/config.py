import logging
import json

'''
Created on Apr 17, 2015
@author: BrickRoad
'''

def getConfig(key):
    with open('config.json') as data_file:
        data = json.load(data_file)
        try:
            return data[key]
        except KeyError:
            logging.warning('Missing key in JSON file' + key)
            return False

def getFullConfig():
    with open('config.json') as data_file:
        data = json.load(data_file)
        return data
