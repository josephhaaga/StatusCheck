import requests;
import re;

google = 'http://google.com';

def checkGoogleAnalytics(url):
	try:
		r = requests.get(url);
		# success
		# print (r.text);

		# Check for Google Analytics tracking code
		m = re.search('UA-\d+', r.text);
		if m:
		    print ("Google Analytics found on "+url);
		else:
			print ("Google Analytics NOT FOUND on "+url);
	except:
		print ("Problem retrieving "+url);

	print ("\n");


checkGoogleAnalytics(google);
checkGoogleAnalytics("http://joehaaga.xyz");