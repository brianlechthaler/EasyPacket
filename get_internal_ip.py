from scapy.all import *

def gateway():
    ipv4 = conf.route.route("0.0.0.0")[2]
    print(ipv4)
    return(ipv4)
