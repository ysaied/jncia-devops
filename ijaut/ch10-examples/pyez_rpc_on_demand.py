#!/usr/bin/python

from jnpr.junos import Device

if __name__ == '__main__':
    dev = Device(host='172.25.11.1', user='lab', passwd='lab123')
    dev.open()
    interface_lxml_element = dev.rpc.get_interface_information(terse=True)
    list_of_interfaces = interface_lxml_element.findall('physical-interface')
    for interface in list_of_interfaces:
        print("Interface: {} Status: {}".format(interface.findtext('name').strip(),
                                             interface.findtext('oper-status').strip()))
    dev.close()

