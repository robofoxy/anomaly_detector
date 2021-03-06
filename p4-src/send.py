#!/usr/bin/env python
import argparse
import sys
import socket
import random
import struct

from scapy.all import sendp, send, get_if_list, get_if_hwaddr
from scapy.all import Packet, Raw
from scapy.all import Ether, IP, UDP, TCP
from time import sleep

def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print "Cannot find eth0 interface"
        exit(1)
    return iface

def main():

    if len(sys.argv)<3:
        print 'pass 2 arguments: <destination> "<input_path>"'
        exit(1)

    addr = socket.gethostbyname(sys.argv[1])
    iface = get_if()
    print "sending on interface %s to %s" % (iface, str(addr))

    filepath = sys.argv[2]
    with open(filepath) as fp:
       line = fp.readline()
       while line:
           pkt =  Ether(src=get_if_hwaddr(iface),dst = "00:00:00:00:01:12")
           pkt = pkt /IP(dst=addr)/TCP(dport=8080)/Raw(load=line.strip())
           pkt.show2()
           sendp(pkt, iface=iface, verbose=False)
           sleep(0.05)
           line = fp.readline()


if __name__ == '__main__':
    main()
