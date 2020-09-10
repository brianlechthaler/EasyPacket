from scapy.all import *

destIP = "127.0.0.1"
dest = destIP

def tcpPortScan(dest):
    msg = "Listen for SYN-ACK, RST or ICMP error after sending TCP SYN to each port on host: " + dest
    print(msg)
    res, unans = sr( IP(dst=dest)
            /TCP(flags="S", dport=(1, 1024)) )
    response = res.nsummary( lfilter=lambda s,r: (r.haslayer(TCP) and (r.getlayer(TCP).flags & 2)) )
    print(response)
    return(response)

