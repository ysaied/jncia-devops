#!/usr/bin/python

# This is a comment
my_interfaces = ['ge-0/0/0', 'xe-1/0/0']

for interface in my_interfaces:
    if interface.startswith('ge-'):
        print("%s is a 1G interface!" % interface)
    elif interface.startswith('xe-'):
        print("%s is a 10G interface!" % interface)
    else:
        print("Couldn't recognize the speed of interface: %s" % interface)

print("Finished testing interfaces!")
