#!/usr/bin/env python
import sys
import struct
import os

from scapy.all import sniff, sendp, hexdump, get_if_list, get_if_hwaddr, bind_layers
from scapy.all import Packet, IPOption, Ether
from scapy.all import ShortField, IntField, LongField, BitField, FieldListField, FieldLenField
from scapy.all import IP, UDP, TCP, Raw, ls
from scapy.layers.inet import _IPOption_HDR

def handle_pkt(pkt):
    print "Controller got a packet"
    sys.stdout.flush()
    try:
        print str(bytes(pkt[TCP].payload))
    except Exception as e:
        print e

def main():

    ifaces = ["s1-cpu-eth1", "s1-eth1"]
    sys.stdout.flush()
    sniff(iface = ifaces, prn = lambda x: handle_pkt(x))
    
if __name__ == '__main__':
    main()
