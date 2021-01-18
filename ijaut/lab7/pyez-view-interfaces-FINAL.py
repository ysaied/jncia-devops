#!/usr/bin/python

from jnpr.junos import Device
from pprint import pprint
from lxml import etree

if __name__ == "__main__":
    with Device("172.25.11.1", user="lab", passwd="lab123") as dev:
        # pprint(dev.facts)

        config_json = dev.rpc.get_config(filter_xml="interfaces",
                                         options={"format": "json"})
        # pprint(config_json)

        print("Configured interfaces:")
        for interface in config_json["configuration"]["interfaces"]["interface"]:
            print(interface["name"])

        print("\nInterface operational status:")
        rpc_result = dev.rpc.get_interface_information()
        # etree.dump(rpc_result)

        interfaces = rpc_result.xpath("physical-interface")
        for interface in interfaces:
            print("Interface: {}, Status: {}".format(
                interface.findtext("name").strip(),
                  interface.findtext("oper-status").strip()))
