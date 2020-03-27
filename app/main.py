import requests
import dateutil.parser
from time import sleep
from bs4 import BeautifulSoup as bs

'''
    Lage en enkel QT applikasjon som viser
        Trondheim
        #Antall smittede
        #Døde
        #Sist oppdatert
    #Horisontalt løpende liste med data fra andre steder i trøndelag
'''

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

def print_data_all_cities():
    cities = get_available_cities()
    for city in cities:
        print_important_data(get_city_info(city))
        print("------------------")
    print("Sist oppdatert: {}".format(get_when_updated().strftime("%b %d %Y %H:%M:%S")))

def print_data_top(num: int=0):
    cities = get_available_cities()

    if num == 0:
        num = len(cities)

    for i in range(num):
        print_important_data(get_city_info(cities[i]))
        print("-----------------------")
    print("Sist oppdatert: {}".format(get_when_updated().strftime("%b %d %Y %H:%M:%S")))
    


def main():

    while(True):
        print_data_top(3)
        sleep(3)
        
        

if __name__ == '__main__':
    main()
print_data_top(3)

