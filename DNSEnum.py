!/bin/python3

import dns.resolver
import sys

record_types = ['A', 'AAAA', 'NS', 'CNAME', 'MX', 'PTR', 'SOA', 'TXT']
try:
	domain = sys.argv[1]
except IndexError:
	print('Syntax Error - python3 DNSEnum.py <domainname>')
	quit()
for records in record_types:
	try:
		answer = dns.resolver.resolve(domain, records)
		print(f'\n{records} Records')
		print('-'*30)
		for server in answer:
		    print(server.to_text() + '\n')
	except dns.resolver.NoAnswer: 
		pass
	except dns.resolver.NXDOMAIN:
		print(f'{domain} does not exist.')
		quit()
	except KeyboardInterrupt:
		quit()
