#!/usr/bin/env python3
""" 
    Author : ayadi mohammed
    Github account : ayadim
    script title : subdomain-shodan-finder
    discription : This script get Subdomains from DNS records collected from shodan.


    How it works 
    1- you should have an API-key for shodan
    2- run it : python3 subdomain-shodan-finder.py domain.com

 """

import requests,json,sys

#check command line input
if len(sys.argv) != 2:
    print("Warning : You should add a domain")
    print("Example : python3 subdomain-shodan-finder.py domain.com")
    exit()


shodan_apikey = "" #change it 
domain = sys.argv[1]
listOfSubdomains={"www"}
link ="https://api.shodan.io/dns/domain/"+domain+"?key="+shodan_apikey

#Request Shodan for data
response = ""
data = ""
try:
    response = requests.get(link)
    data = response.json()
    response = requests.get(link)
    data = response.json()
except Exception:
    print("Check that your api key is valid.")
    exit()



for item in data["data"]:
    listOfSubdomains.add(item["subdomain"])

for item in listOfSubdomains:
    if item != "":
        print(item+"."+domain)
