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

shodan_apikey = "" #change it 
domain = sys.argv[1]
listOfSubdomains={"www"}
link ="https://api.shodan.io/dns/domain/"+domain+"?key="+shodan_apikey

#Request Shodan for data
response = requests.get(link)
data = response.json()
for item in data["data"]:
    listOfSubdomains.add(item["subdomain"])

for item in listOfSubdomains:
    print(item+"."+domain)
