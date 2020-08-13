import requests
from bs4 import BeautifulSoup


world_url= str("https://www.worldometers.info/coronavirus")
india_url = str("https://www.worldometers.info/coronavirus/country/india/")

soup = BeautifulSoup(requests.get(world_url).text, "html.parser")
soup1 = BeautifulSoup(requests.get(india_url).text, "html.parser")

value = soup.findAll("div", {"class": "maincounter-number"})
value += soup.findAll("div", {"class": "number-table-main"})

value1 = soup1.findAll("div", {"class": "maincounter-number"})
value1 += soup1.findAll("div", {"class": "number-table-main"})

values = list()
values1 = list()

for x in value:
     values.append(x.text.strip())

tot_cases = str(values[0])
tot_deaths = str(values[1])
tot_recovered = str(values[2])
active_cases = str(values[3])
closed_cases = str(values[4])

for x in value1:
     values1.append(x.text.strip())

tot_cases1 = str(values1[0])
tot_deaths1 = str(values1[1])
tot_recovered1 = str(values1[2])
active_cases1 = str(values1[3])
