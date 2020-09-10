from scapy.all import *

#set interface to whatever the default interface is
iface = conf.iface

def macAddr(iface):
    mac = get_if_hwaddr(iface)
    print(mac)
    return(mac)
