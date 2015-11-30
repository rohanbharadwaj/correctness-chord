from twisted.internet import reactor
from twisted.python import log
from kademlia.network import Server
import sys
import random
import pickle

log.startLogging(sys.stdout)

if len(sys.argv) != 4:
    print "Usage: python driver.py <bootstrap ip> <bootstrap port> <num_nodes>"
    sys.exit(1)

ip = sys.argv[1]
port = int(sys.argv[2]) # 8468 server.tac
num_nodes = int(sys.argv[3])


# print "Getting %s (with bootstrap %s:%i)" % (key, ip, port)

# def done(result):
#     # print "Key result:"
#     # print result
#     reactor.stop()

def bootstrapDone(found, server):
    if len(found) == 0:
        print "Could not connect to the bootstrap server."
        # reactor.stop()
    # server.get(key).addCallback(done)

# num_nodes = 5
nodes = {}
nodes =  random.sample(range(8500,8889),num_nodes)
pickle.dump(nodes,open("node_ports.pickle","w"))
print "Starting %i nodes on ports - %s" % (num_nodes,nodes)
print "bootstrap %s:%i" % (ip,port)
for node in nodes: 
	server = Server()
	server.listen(node)
	server.bootstrap([(ip, port)]).addCallback(bootstrapDone, server)

# server = Server()
# server.listen(8568)
# server.bootstrap([(ip, port)]).addCallback(bootstrapDone, server, key)

reactor.run()
