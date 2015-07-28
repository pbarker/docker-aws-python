from dns import records
from config import config
import logging
import os
import boto.route53
import argparse


# #

#Arguments
import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-n","--name",
                    help="name of instance")
parser.add_argument("-s", "--size", choices=['micro',''],
                    help="size of ec2 instance")
parser.add_argument("-r", "--repo",
                    help="docker repo to be installed")
args = parser.parse_args()
name = args.name
size = args.size
repo = args.repo

# Logging
logLocation = config.getConfig('logLocation')
logger = logging.getLogger('AWS-DNS-Simple')
hdlr = logging.FileHandler(logLocation)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)


# #
# Records
a = records.getAAlias()
c = records.getCAlias()
ip = records.getPublicIp()

# #
# AWS API
# Pick up here
os.environ['AWS_ACCESS_KEY_ID'] = config.getConfig('awsKey')
os.environ['AWS_SECRET_ACCESS_KEY'] = config.getConfig('awsSecret')
conn = boto.route53.connect_to_region('us-west-2')
zone = conn.get_zone(config.getConfig('domain'));
# A
fullAAlias = a + '.' + config.getConfig('domain')
try:
    zone.add_a(fullAAlias, ip, config.getConfig('ttl'))
except boto.route53.exception.DNSServerError:
    zone.update_a(fullAAlias, ip, config.getConfig('ttl'))

# C
try:
    zone.add_cname(c, fullAAlias, config.getConfig('ttl'))
except boto.route53.exception.DNSServerError:
    zone.update_cname(c, fullAAlias, config.getConfig('ttl'))

# Need to add functionality for other names

