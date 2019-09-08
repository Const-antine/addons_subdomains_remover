#!/bin/usr/env python

import subprocess
import sys,json



e = ""

#Defining cPanel user to proceed with
un = raw_input("Please enter the cPanel user: ")

#main function to call uAPI and list subdomains and add-ons
def ls_sub_func():

  p = subprocess.Popen(['uapi', '--user=%s'% (un), 'DomainInfo', 'list_domains', '--output=json'], stdout=subprocess.PIPE,
  stderr=subprocess.PIPE)
  o,e = p.communicate()

  if e and "You do not have a user named" in e:
    print("%s user was not found. Please double-check it." % (un))

  elif e:
        	print("The following errors occurred: \n")
        	print(e)
        	return o

  else:
		      return o
# function to call CpAPI2. It is run only if you are goind to remove add-ons. It is used to pick available add-ons AND subdomains of this add-ons
def ls_add_func():
  p = subprocess.Popen(['cpapi2', '--user=c0nst', 'AddonDomain', 'listaddondomains', '--output=json'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
  o,e = p.communicate()
  if e:
    print("The following errors occurred: \n")
    print(e)
    return o
  else:  
	  return o





try:
#defining a var and processing a JSON output
  o = ls_sub_func()
  a = json.loads(o)
  sdoms = a["result"]["data"]["sub_domains"]
  addons = a["result"]["data"]["addon_domains"]
  
  print("The following add-ons were found for %s user \n" % (un))
  for i in addons:
	  print("%s" % (i))


  print("The following subdomains were found for %s user \n" % (un))
  for i in sdoms:
	  print("%s" % (i))

# Here we should decide what we are going to work with
  bul = raw_input("Are you sure you want to proceed? \n If so, please type 'A' to remove add-ons and 'S' - subdomains \n")

  if bul == "S":
    for i in sdoms:
      b = subprocess.call(['cpapi2', '--user=%s'% (un), 'SubDomain', 'delsubdomain', 'domain=%s' % (i)])
      print("%s - Removed" % (i))

# If we choose A, we call the ls_add_func function and remove tha add-ons
  elif bul == "A":
    out = ls_add_func()
    adds = json.loads(out)
    b = len(adds['cpanelresult']['data'])
    v = range(b)
    for i in v:
      dom = (adds['cpanelresult']['data'][i]['domain'])
      sa = (adds['cpanelresult']['data'][i]['fullsubdomain'])
#Add-ons are being removed herei
      de = subprocess.call(['cpapi2', '--user=%s' % (un), 'AddonDomain', 'deladdondomain', 'domain=%s' % (dom), 'subdomain=%s' % (sa)])
      print('%s - removed' % dom)
  else:
    print('Break!')
except Exception:
  print("Some errors were found in the output")
