from twisted.internet import reactor
from twisted.python import log
from kademlia.network import Server
import sys
import random

log.startLogging(sys.stdout)

if len(sys.argv) != 5:
    print "Usage: python query.py <bootstrap ip> <bootstrap port> <key> <value>"
    sys.exit(1)

ip = sys.argv[1]
port = int(sys.argv[2])
key = sys.argv[3]
value = sys.argv[4]


def done(result):
    print "Key result:", result
    reactor.stop()

def setDone(result, server):
    server.get(key).addCallback(done)

def bootstrapDone(found, server):
    server.set(key, value).addCallback(setDone, server)

server = Server()
temp_port = random.randint(9000,9999)
server.listen(temp_port) #  Any node wishing to query the network essentially registers itself as a server/node with every node it communicates with
server.bootstrap([(ip, port)]).addCallback(bootstrapDone, server)

reactor.run()
