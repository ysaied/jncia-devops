#!/usr/bin/python

from jnpr.junos import Device
from jnpr.junos.utils.config import Config
from jnpr.junos.exception import *

if __name__ == '__main__':
    try:
        dev = Device(host='172.25.11.1', user='lab', passwd='lab123')
        dev.open()
        conf = Config(dev)
        conf.lock()
        conf.load(path="bgp-config.conf", merge=True)
        conf.commit()
        conf.unlock()
        print("Configuration applied!")
    except ConnectAuthError:
        print("Authentication error!")
    except ConnectTimeoutError:
        print("NETCONF connection timed out!")
    except ConnectError as error:
        print("Other connect error: %s" % str(error))
    except ConfigLoadError:
        print("Failure when loading a configuration!")
    except Exception as error:
        print("Some other exception happened: %s" % str(error))
    finally:
        dev.close()

