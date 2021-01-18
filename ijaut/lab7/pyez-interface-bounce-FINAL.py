#!/usr/bin/python

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from time import sleep

if __name__ == "__main__":
    with Device("172.25.11.1", user="lab", passwd="lab123") as dev:
        with Config(dev, mode="exclusive") as conf:
            print("Disabling the interface...")
            conf.load("set interfaces ge-0/0/0 disable", format="set")
            conf.pdiff()
            conf.commit()
            print("Commit complete, waiting...")
            sleep(5)
            print("Enabling the interface...")
            conf.load("delete interfaces ge-0/0/0 disable", format="set")
            conf.pdiff()
            conf.commit()
            print("Finished!")
