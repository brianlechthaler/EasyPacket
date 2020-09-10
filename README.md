# EasyPacket

Scapy made simple

## Disclaimer

What you do with EasyPacket is 100% *your responsibility*. Some of the tools/scripts included in this repo can probably be used to do some pretty dangerous stuff, so don't use anything here on systems you're not explicitly authorized to use EasyPacket on. Remember, it's all fun and games -- until there's an arrest warrant with your name on it.

## Using EasyPacket with IPython
1) Clone this repo: `git clone https://github.com/brianlechthaler/EasyPacket.git`

2) `cd` into this repo: `cd EasyPacket`

3) Run IPython as user `root` with `sudo`: `sudo ipython`

4) `import` an EasyPacket module into your namespace: `[1] import tcp_port_scan`

5) Run EasyPacket module with required `dest`ination IP argument: `tcp_port_scan.tcpPortScan(dest="127.0.0.1")`

## Currently Implemented Functions

* ARP Ping: `arp_ping.py`

* TCP Port Scanner: `tcp_port_scan.py`

* Get internal IP address: `get_internal_ip.py`
