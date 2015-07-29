from dns import records
from config import config
import logging
import os
import boto.route53
import argparse


##
#Arguments
#
# Patrick can you please support all of the following arguments? with the indented value on the following row is what they will default to if nothing is passed?
#
# region <string> http://docs.aws.amazon.com/general/latest/gr/rande.html#ec2_region (Under region column, us-east-1, us-west-1, etc)
#     us-west-1
# cname <string> Any string, the script can be smart enough to point the c record at the a name EX: sub.mydomain.com
#     null
# size <string> Here are all the amazon instance sizes, http://aws.amazon.com/ec2/instance-types/, I would probably only want to support the general purpose instances for now Ex: t2.micro, t2.small, etc
#     t2.micro
# securitygroup <string> We should build in support for this, just accepts the security group ID to build this server in
#     null
# os <string> I would dumb this down and only support redhat, amazon, ubuntu, suse (all 64)
#     amazon
# drivesize <int> Gb of the main /dev/xvda volume
#     8
#

parser = argparse.ArgumentParser()
parser.add_argument("-n","--name",
                    help="name of instance")
parser.add_argument("-s", "--size", choices=['micro',''],
                    help="size of ec2 instance")
parser.add_argument("-i", "--instance",
                    help="docker image to be installed")
parser.add_argument("-r", "--region",
                    help="region of server location")
parser.add_argument("-g", "--securitygroup",
                    help="Security group ID")
parser.add_argument("-o", "--os",
                    help="Server Operating System")
parser.add_argument("-d", "--drivesize", type=int,
                    help="Drive Size in GB of main /dev/xvda volume")

args = parser.parse_args()
name = args.name
size = args.size
instance = args.instance
region = args.region
security =  args.securitygroup
os = args.os
drivesize = args.drivesize

# Logging
logLocation = config.getConfig('logLocation')
logger = logging.getLogger('docker-aws-python')
hdlr = logging.FileHandler(logLocation)
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr)
logger.setLevel(logging.DEBUG)


# #
# Records
# a = records.getAAlias()
# c = records.getCAlias()
# ip = records.getPublicIp()

# #
# START AWS Code here
# Pick up here
# These need to be environmental variables set
# TODO we need a check here
os.environ['AWS_ACCESS_KEY_ID'] = config.getConfig('awsKey')
os.environ['AWS_SECRET_ACCESS_KEY'] = config.getConfig('awsSecret')



conn = boto.route53.connect_to_region('us-west-2')
zone = conn.get_zone(config.getConfig('domain'));
# A
'''
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
'''

