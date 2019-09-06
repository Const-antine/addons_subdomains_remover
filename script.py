#!/bin/usr/env python

import subprocess
import sys,json



e = ""

def func():

	p = subprocess.Popen(['uapi', '--user=c0nst', 'DomainInfo', 'list_domains', '--output=json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	o,e = p.communicate()
	


	if e:
        	print("The following errors occurred: \n")
        	print(e)
        	ans =  raw_input("Should I proceed? ")
        	if ans == "Y":
			print('proceeding')
			return o
		else:
			return 

#if e:
#	print("The following errors occurred: \n")
#	print(e)
#	ans =  raw_input("Should I proceed? ")
#	if ans == "Y":




func()
a = json.loads(o)
sdoms = a["result"]["data"]["sub_domains"]
addons = a["result"]["data"]["addon_domains"]
print(sdoms)
print(addons)
		

for i in addons:
	print("%s" % (i))

for i in sdoms:
	print("%s" % (i))


bul = raw_input("Are you sure you want to remove all these pretties? ")

if bul == "Y":
	for i in sdoms:
		print("Removed")
else:
	print('Break!') 
#	else:
#		print('Break!')

#else: 
#	print('Break!')
