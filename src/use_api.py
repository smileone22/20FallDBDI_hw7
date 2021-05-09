import urllib.request
import json
import requests

serviceurl='https://api64.ipify.org?format=json'

data = urllib.request.urlopen(serviceurl).read().decode()
js = json.loads(data)
ip_a=str(js['ip'])
print("PUBLIC IP: ",ip_a)