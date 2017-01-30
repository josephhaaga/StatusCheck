import requests;
import re;


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
	except:
		try:
			r = requests.get(url,verify=False);
			# success

			# Check for Google Analytics tracking code
			m = re.search('UA-\d+', r.text);
			if m:
			    print ("Google Analytics found on "+url);
			    return True;
			else:
				print ("Google Analytics NOT FOUND on "+url);
				return False;
		except:
			print ("Problem retrieving "+url);

	return False;
