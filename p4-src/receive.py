#!/usr/bin/env python
import sys
import struct
import os

import pickle

from scapy.all import sniff, sendp, hexdump, get_if_list, get_if_hwaddr, bind_layers
from scapy.all import Packet, IPOption, Ether
from scapy.all import ShortField, IntField, LongField, BitField, FieldListField, FieldLenField
from scapy.all import IP, UDP, TCP, Raw, ls
from scapy.layers.inet import _IPOption_HDR

sys.path.append('../')
from scripts.import_data import *

i = 0
def handle_pkt(pkt, clf):
    # print "Controller got a packet"
    # sys.stdout.flush()
    global i
    try:
        pkt_features = str(bytes(pkt[TCP].payload))
        if pkt_features:
            test_x = encode_feature_vector(pkt_features)
            test_y = pkt_features.split(",")[-1]
            # print pkt_features
            # print test_x
            prediction = clf.predict(np.array([test_x]))
            print i, decode_label(prediction), prediction , "actual label:" , test_y
            i+=1
    except Exception as e:
        print e

def main():
    if len(sys.argv) < 2:
        print "usage: ./" +  sys.argv[0] + " <trainedModelDumpPath>"
        exit(1)

    # Load from file
    clf = pickle.load(open(sys.argv[1], 'rb'))
    print clf
    ifaces = ["s1-cpu-eth1", "s1-eth1"]
    sys.stdout.flush()
    sniff(iface = ifaces, prn = lambda x: handle_pkt(x, clf))

if __name__ == '__main__':
    main()
