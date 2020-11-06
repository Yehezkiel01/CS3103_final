from dnslib.server import DNSServer, DNSLogger
from dnslib.dns import DNSRecord, RR
import time

DNS_SERVER_IP_ADDRESS = "127.0.0.1"
PORT = 5000
TEST = True
db = None

import sqlite3

def get_database_path():
    return './database/dns.db'

# Reference: https://flask.palletsprojects.com/en/1.1.x/patterns/sqlite3/
# Get the current db or created a new connection if there is no db yet
def get_db():
    global db
    if db is None:
        db = sqlite3.connect(get_database_path())
    return db

def close_connection():
    global db
    if db is not None:
        db.close()
        db = None

# Execute one line of sql statement
# which may consists of more than one statement
def execute_sql_statement(sql_statement):
    statements = sql_statement.split(';')
    results = []

    cur = get_db().cursor()
    for s in statements:
        print("[LOG] executing statement: " + s)
        cur.execute(s)
        get_db().commit()
        results += cur.fetchall()
    cur.close()
    close_connection()

    return results

# Open connection with sql to query the domain
def dummy_sql_query(domain):
    # Removing the last character, which is a dot, of the domain
    domain_name = str(domain).replace("www.", "") # Remove www.
    domain_name = domain_name[:-1]
    sql_query = "SELECT * FROM records WHERE domain='" + domain_name + "';"
    print("[LOG] SQL Query: " + sql_query)
    results = execute_sql_statement(sql_query)
    print("[LOG] Raw Results: " + str(results))

    if (len(results) == 0):
        return None

    (domain, ip) = results[0]
    return ip

class BasicResolver:
     def resolve(self,request,handler):
         domain_query = request.get_q().get_qname()
         ip_address = dummy_sql_query(domain_query)
         reply = request.reply()
         reply.add_answer(*RR.fromZone(f"{domain_query} 60 A {ip_address}"))
         return reply

resolver = BasicResolver()
logger = DNSLogger(prefix=False)
server = DNSServer(resolver, port=PORT, address=DNS_SERVER_IP_ADDRESS, logger=logger)
server.start_thread()

# Testing
if TEST:
	print("Testing connection...")
	q = DNSRecord.question("www.bank.com")
	print("Sending request to server...\n")
	a = q.send(DNS_SERVER_IP_ADDRESS, PORT)
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