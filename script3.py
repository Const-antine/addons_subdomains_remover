#!/bin/usr/env python

import subprocess
import sys,json



e = ""

#Defining cPanel user to proceed with
un = raw_input("Please enter the cPanel user: ")

#main function to call uAPI command from shell
def func():

	p = subprocess.Popen(['uapi', '--user=%s'% (un), 'DomainInfo', 'list_domains', '--output=json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	o,e = p.communicate()
	


	if e:
        	print("The following errors occurred: \n")
        	print(e)
        	return o

	else:
		return o



#defining a var and processing a JSON output
o = func()
a = json.loads(o)
sdoms = a["result"]["data"]["sub_domains"]
addons = a["result"]["data"]["addon_domains"]
print(sdoms)
print(addons)
		
print("The following add-ons were found for %s user \n" % (i))
for i in addons:
	print("%s" % (i))


print("The following subdomains were found for %s user \n" % (i))
for i in sdoms:
	print("%s" % (i))


bul = raw_input("Are you sure you want to proceed? \n If so, please type 'A' to remove add-ons and 'S' - subdomains \n")

if bul == "S":
  for i in sdoms:
    print("%s - Removed" % (i))
elif bul == "A":
  for i in addons:
    print("%s - Removed" % (i))
else:
  print('Break!') 

