import requests
import json
import time
rg = requests.get('https://coronavirus-19-api.herokuapp.com/countries')
data = rg.json()

ct = data[33]['country']
total_cases = data[33]['cases']
total_deaths = data[33]['deaths']
today_cases = data[33]['todayCases']
today_deaths = data[33]['todayDeaths']
recovered = data[33]['recovered']
total_tests = data[33]['totalTests']

print("------ Covid 19 Stats ",ct,"-------")
print("Today Cases: ",today_cases)
print("Today Death: ",today_deaths)
print("Total Test: ",total_tests)
print("Total Cases: ",total_cases)
print("Total Death: ",total_deaths)
print("Total Recovered: ",recovered)
