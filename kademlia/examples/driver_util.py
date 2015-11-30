# Reference : http://findingscience.com/python/kademlia/dht/2014/02/14/kademlia:-a-dht-in-python.html
from twisted.internet import reactor
from twisted.python import log
from kademlia.network import Server
import sys
import random

log.startLogging(sys.stdout)


def getKey(ip,port,key):
	def done(result):
	    print "Key result:"
	    print result
	    reactor.stop()

	def bootstrapDone(found, server, key):
	    if len(found) == 0:
	        print "Could not connect to the bootstrap server."
	        reactor.stop()
	    server.get(key).addCallback(done)

	server = Server()
	temp_port = random.randint(9000,9999)
	server.listen(temp_port) #  Any node wishing to query the network essentially registers itself as a server/node with every node it communicates with
	server.bootstrap([(ip, port)]).addCallback(bootstrapDone, server, key)

	reactor.run()
