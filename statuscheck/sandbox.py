import functions;
import os;
from time import sleep

list_of_sites = open(os.path.dirname(os.path.abspath(__file__))+'/settings.conf');

for n in list_of_sites:
	sleep(1);
	m = n.replace("\n","");
	functions.check_google_analytics(m);

