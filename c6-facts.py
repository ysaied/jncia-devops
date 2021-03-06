#!/usr/bin/python
from jnpr.junos import Device
from pprint import pprint


dev_mgmt = { "KIF_VPN" : "10.117.97.56", 
   "HRZ_VPN" : "10.117.97.55", 
   "AMS_VPN" : "10.117.97.37", 
   "LON_VPN" : "10.117.97.36", 
   "Partner" : "10.117.97.39"
   } 

login_username = "ysaied"

for src_node, mgmt_ip in dev_mgmt.items():
   dev = Device(host= mgmt_ip, user= login_username)
   dev.open()
   print ( "="*20 + src_node + "="*20)
   dev_info = dev.facts
   pprint (dev_info)
   print ("="*20 + "="*len(src_node)  + "="*20)
   dev.close()
