import re

from twisted.internet import reactor
from twisted.names import dns
from twisted.names import client, server

dev_pattern = r'^[\w\-\.]+\.dev$'
dev_address = '127.0.0.1'
dev_ttl = 60
fwd_resolvers = [
    ('8.8.8.8', 53),
    ('8.8.4.4', 53)
]

class DNSServerFactory(server.DNSServerFactory):    
    def handleQuery(self, message, protocol, address):
        query = message.queries[0]
        if query.type == dns.A and re.search(dev_pattern, query.name.name) != None:
            message.rCode = dns.OK
            message.answers = [
                dns.RRHeader(bytes(query.name.name),
                    dns.A, dns.IN, dev_ttl, dns.Record_A(dev_address, dev_ttl))
            ]
            return self.sendReply(protocol, message, address)
        return server.DNSServerFactory.handleQuery(self, message, protocol, address)


if __name__ in '__builtin__':
    verbosity = 1
    
    resolver = client.Resolver(servers=fwd_resolvers)
    factory = DNSServerFactory(clients=[resolver], verbose=verbosity)
    protocol = dns.DNSDatagramProtocol(factory)
    factory.noisy = protocol.noisy = verbosity
    
    reactor.listenUDP(53, protocol)
    reactor.listenTCP(53, factory)
    reactor.run()
