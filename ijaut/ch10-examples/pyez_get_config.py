#!/usr/bin/python

from jnpr.junos import Device
from lxml import etree

if __name__ == '__main__':
    with Device(host='172.25.11.1', user='lab', passwd='lab123') as dev:
        cnf = dev.rpc.get_config(filter_xml=etree.XML('<configuration><interfaces/></configuration>'))
        print(etree.tostring(cnf))
