#!/usr/bin/python
from jnpr.junos import Device
from pprint import pprint
from lxml import etree
from jnpr.junos.utils.config import Config


dev_mgmt = { "KIF_VPN" : "10.117.97.56", 
   "HRZ_VPN" : "10.117.97.55", 
   "AMS_VPN" : "10.117.97.37", 
   "LON_VPN" : "10.117.97.36", 
   "Partner" : "10.117.97.39"
   } 

login_username = "ysaied"

original_rpc = """
<get-config>
  <source><running/></source>
  <filter type="subtree">
    <configuration>
      <system>
        <login/>
      </system>
    </configuration>
  </filter>
</get-config>
"""

getconf_filter_string = """
<configuration>
  <system>
    <name-server/>
  </system>
</configuration>
"""

xml_filter = etree.XML(getconf_filter_string)

setconf_dns = """
<system>
  <name-server>
    <name>8.8.8.8</name>
  </name-server>
  <name-server>
    <name>8.8.4.4</name>
  </name-server>
</system>
"""


for src_node, mgmt_ip in dev_mgmt.items():
   dev = Device(host= mgmt_ip, user= login_username)
   dev.open()
   print ( "="*20 + src_node + "="*20)

   show_dns_conf = dev.rpc.get_config(filter_xml=xml_filter)
   
   if ( show_dns_conf.find('system/name-server') is None ):
      print ("NO DNS configured, DNS configuration to be pushed!")
      conf = Config(dev)
      conf.lock()
      conf.load(setconf_dns)
      conf.commit()
      conf.unlock()
      print ("DNS configuration pushed successfully!")
   else:
      print ("DNS configuration found as below (formal XML):")
      print (etree.tostring(show_dns_conf, encoding='unicode', pretty_print=True))

   print ("="*20 + "="*len(src_node)  + "="*20)
   dev.close()
