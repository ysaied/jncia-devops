#!/usr/bin/python

from jnpr.junos import Device
from jnpr.junos.utils.config import Config

if __name__ == '__main__':

    data = 'set system services netconf traceoptions file test.log'
    with Device(host='172.25.11.1', user='lab', passwd='lab123') as dev:     
        with Config(dev, mode="exclusive") as conf:
            conf.load(data, format='set', merge=False, overwrite=False)
            diff = conf.diff()
            if diff is None:
                print("Configuration already up to date.")
            else:
                print(diff)
                conf.commit()   
