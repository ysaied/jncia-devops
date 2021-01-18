
from jnpr.junos import Device
from jnpr.junos.utils.sw import SW

USER = "lab"
PASSWD = "lab123"
DEVICE_IP = "172.25.11.1"
PACKAGE = "/var/tmp/junos-openconfig-x86-32-0.0.0.9.tgz"

def progress_callback(dev, report):
    print(report)

dev = Device(host=DEVICE_IP, user=USER, password=PASSWD)
dev.open()

sw = SW(dev)

ok = sw.install(package=PACKAGE, no_copy=True, validate=False,
             progress=progress_callback)

dev.close()

# print(ok)

# sw.reboot()

