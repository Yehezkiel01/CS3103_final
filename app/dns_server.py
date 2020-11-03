from dnslib.server import DNSServer, DNSLogger
from dnslib.dns import DNSRecord, DNSQuestion, RR
import time

DNS_SERVER_IP_ADDRESS = "127.0.0.2"
PORT = 53
TEST = True

"""

    To create class for this file and host from app.py
    -- DNS_server.start()
    
    Running this python script will require `sudo` if hosting on reserved ports (such as 53)

"""

def dummy_sql_query(domain):
	# query sql
	# return ip address from sql
	return "127.0.0.1"


class BasicResolver:
     def resolve(self,request,handler):
         domain_query = request.get_q().get_qname()
         ip_address = dummy_sql_query(domain_query)
         reply = request.reply()
         reply.add_answer(*RR.fromZone(f"abc.def. 60 A {ip_address}"))
         return reply
         
resolver = BasicResolver()
logger = DNSLogger(prefix=False)
server = DNSServer(resolver, port=PORT, address=DNS_SERVER_IP_ADDRESS, logger=logger)
server.start_thread()

# Testing
if TEST:
	print("Testing connection...")
	q = DNSRecord.question("google.com")
	print("Sending request to server...\n")
	a = q.send("127.0.0.2", 53)
	print("\n\nParsing reply from server...\n")
	print(DNSRecord.parse(a))
	time.sleep(2)
	print("Test done...")
	time.sleep(1)
	print("\n"*20)

print(f"Hosting server at {DNS_SERVER_IP_ADDRESS}:{PORT}")
print("Ctrl-C to stop server...")
while True:
	pass