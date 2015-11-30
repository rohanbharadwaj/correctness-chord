# Reference : http://findingscience.com/python/kademlia/dht/2014/02/14/kademlia:-a-dht-in-python.html
#!/usr/bin/env python

"""kademila_test_driver.py: Test suite to test correctness of kademila ."""

__author__      = "Rohan Bharadwaj"

import random
import hashlib
import unittest

import sys
import random
import os
import pickle
import subprocess
import thread
import time

class TestKademila(unittest.TestCase):
    nodes = {}
    def setUp(self):
        """
        setup: 
        1. run setup.sh
        2. create nodes in chord 
            python driver.py 127.0.0.1 8468 5 (python driver.py <bootstrap_ip> <port> <num_nodes>)
        """
        nodes = pickle.load(open("node_ports.pickle","r"))
        print nodes
        node0 = list(nodes)[0]
        node1 = list(nodes)[1]
        os.system('python store.py 127.0.0.1  '+str(node0)+' fname rohan')
        os.system('python store.py 127.0.0.1  '+str(node1)+' lname bharadwaj')
        
    def test_get0(self):
        os.system('python query.py 127.0.0.1 8468 fname')
        f = open('newfile.txt')
        expected = f.readline()
        self.assertEqual("rohan",expected)

    def test_get1(self):
        os.system('python query.py 127.0.0.1 8468 lname')
        f = open('newfile.txt')
        expected = f.readline()
        self.assertEqual("bharadwaj",expected)

    def test_get3(self):
        os.system('python query.py 127.0.0.1 8468 X')
        f = open('newfile.txt')
        expected = f.readline()
        self.assertEqual("TypeError",expected) 
  


if __name__ == '__main__':
    unittest.main()