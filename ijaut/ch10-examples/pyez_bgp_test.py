#!/usr/bin/python

from jnpr.junos import Device

if __name__ == '__main__':
    peers_established = 0
    peers_other = 0
    dev = Device(host='172.25.11.1', user='lab', passwd='lab123')
    dev.open()
    bgp_data = dev.rpc.get_bgp_summary_information()
    neighbor_states = bgp_data.xpath("bgp-peer/peer-state")
    for state in neighbor_states:
        if state.text == "Established":
            peers_established += 1
        else:
            peers_other += 1
    dev.close()
    print("Sessions in Established state: {} out of {}".
            format(peers_established, peers_established+peers_other))
    if peers_other != 0:
        print("Warning: there are sessions not in Established state!")
        exit(1)
