import random
import hashlib

from twisted.trial import unittest

# Reference : http://findingscience.com/python/kademlia/dht/2014/02/14/kademlia:-a-dht-in-python.html
from twisted.internet import reactor
from twisted.python import log
from kademlia.network import Server
import sys
import random
# import examples.driver_util


class KademilaTest(unittest.TestCase):
    def test_get(self):
        expected = "rohan"
        key = "A"
        # getkey("127.0.0.1",8468,key)
        # self.assertEqual(expected,result)
        def done(result):
            # print "Key result:"
            # print result
            self.assertEqual(expected,result)
            reactor.stop()

        def bootstrapDone(found, server, key):
            if len(found) == 0:
                print "Could not connect to the bootstrap server."
                reactor.stop()
            server.get(key).addCallback(done)

        server = Server()
        temp_port = random.randint(9000,9999)
        server.listen(temp_port) #  Any node wishing to query the network essentially registers itself as a server/node with every node it communicates with
        server.bootstrap([("127.0.0.1", 8468)]).addCallback(bootstrapDone, server, key)

        reactor.run()