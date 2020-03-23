import requests
import dateutil.parser
from bs4 import BeautifulSoup as bs

#setup
url = "spesial.adressa.no/api/covid19trd"
r = requests.get(url= "https://" + url, headers={"Authorization":"B9329CEF38B2F"})
f_json = r.json()

#returns list of dicts with info regarding each city
def get_data():
    return f_json['data']['data']

#return when the data was last updated as datetime.datetime object
def get_when_updated():
    iso_time = f_json['data']['updated']
    t_obj = dateutil.parser.isoparse(iso_time)
    return t_obj

#returns dictionary for city
def get_city_info(city):
    data = get_data()
    for item in data:
        if item['navn'] == city:
            return item

#takes a city dict and prints the important fields
def print_important_data(city_dict):
    print("\t"+ city_dict['navn'])
    print("Antall smittede: {}".format(city_dict['smittet']))
    print("Antall døde: {}".format(city_dict['dode']))
    print("Sist oppdatert: {}".format(get_when_updated().strftime("%b %d %Y %H:%M:%S")))

def get_available_cities():
    data = get_data()
    cities = []
    for item in data:
        cities.append(item['navn'])
    return cities

def get_county_total_infected():
    data = get_data()
    total = 0
    for item in data:
        total += int(item['smittet'])
    return total

trd_dict = get_city_info('Trondheim')
print_important_data(trd_dict)
print(get_available_cities())
print(get_county_total_infected())