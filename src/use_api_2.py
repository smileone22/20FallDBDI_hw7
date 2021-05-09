import urllib.request
import json
import requests

#accepts country as an input(case sensitive, very sensitive) and returns live data regarding covid19
serviceurl='https://covid-api.mmediagroup.fr/v1/cases?country='
country = input("Enter a country    :")
r = requests.get(serviceurl+country)
js = json.loads(r.content.decode())
print("---------COVID19 in ",country,"------------")
print("Confirmed cases  :",js['All']['confirmed'])
print("Recovered cases  :",js['All']['recovered'])
print("Number of deaths :",js['All']['deaths'])

#"Korea, South"
#"France"