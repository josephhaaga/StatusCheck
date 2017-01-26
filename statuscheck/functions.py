import requests;
import re;

google = 'http://google.com';

def check_google_analytics(url):
	try:
		r = requests.get(url);
		# success

		# Check for Google Analytics tracking code
		m = re.search('UA-\d+', r.text);
		if m:
		    print ("Google Analytics found on "+url);
		    return True;
		else:
			print ("Google Analytics NOT FOUND on "+url);
			return False;
	except (E):
		print (E);
		print ("Problem retrieving "+url);

	return False;
