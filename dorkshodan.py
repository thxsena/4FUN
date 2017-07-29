import shodan

SHODAN_API_KEY = "CL1rYGmEAc7hP8ZjVKxJkmfzqE64yQwN"

api = shodan.Shodan(SHODAN_API_KEY)

try:
	
	dork = raw_input("Dork: ")
	
	results = dork
	results = api.search(dork)
	
	print 'Results Found: %s' % results['total']
	print ""
	
	for result in results['matches']:
		print 'IP: %s' % result['ip_str']
		print 'Organization: %s' % result.get('org', 'n/a')
		print 'Operating system: %s' % result.get('os', 'n/a')
		print 'Port: %s' % result['port']
		print''
except shodan.APIError, e:
	print 'Error: %s' % e
