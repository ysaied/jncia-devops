
#! /usr/bin/python

import requests
from lxml import etree

USER = "lab"
PASSWORD = "lab123"
DEVICES = ["172.25.11.1", "172.25.11.2"]

CONFIG_FILTER = """
<get-config>
  <source>
    <running/>
  </source>
  <filter type="subtree">
    <configuration>
      <system>
        <services/>
      </system>
    </configuration>
  </filter>
</get-config> """

if __name__ == "__main__":

    for device in DEVICES:

        response = requests.post("http://{}:3000/rpc".format(device), data=CONFIG_FILTER,
            auth=requests.auth.HTTPBasicAuth(USER, PASSWORD),
            headers={"Accept": "application/xml", "Content-Type": "application/xml"}
        )

        XML_lines = "\n".join(response.text.splitlines()[3:-1])
        # print(XML_lines)

        resp_XML = etree.fromstring(XML_lines)

        telnet_enabled = len(resp_XML.xpath("configuration/system/services/telnet")) != 0
        ftp_enabled = len(resp_XML.xpath("configuration/system/services/ftp")) != 0

        if telnet_enabled or ftp_enabled:
            print("Warning: Device {} has disallowed service enabled".format(device))
        else:
            print("Device {} is ok".format(device))

