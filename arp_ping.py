from scapy.all import *

destIP = "127.0.0.1"
dest = destIP

def arpPing(dest):
    msg = "Sending ARP Ping Packets to: " + dest
    print(msg)
    arppinger = sr(IP(dst=dest, proto=(1,254)))
    arppinger
