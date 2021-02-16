'''
    Data models:
        load and supply json data
'''

import requests
import json
import dateutil.parser
import datetime

class COVID:
    
    def __init__(self):
        self.url = "spesial.adressa.no/api/covid19trd"
        self.data = []
        self.last_updated = 'NaN'

        self.update()

    def update(self):
        try:
            print("Requesting data from Adressa...")
            r = requests.get(url= "https://" + self.url, headers={"Authorization":"B9329CEF38B2F"})
        except requests.exceptions.RequestException as e:
            print(e)
            return
        try:
            raw_data = r.json()
        except json.JSONDecodeError as e:
            print(e)
            print(r.content)
            return
        print("Updating {} data...".format(self.__class__.__name__))
        self.data = self._prepare_data(raw_data)
        iso_time = raw_data['data']['updated']
        last_update = dateutil.parser.isoparse(iso_time)
        self.last_updated = last_update + datetime.timedelta(hours=1)

    def _prepare_data(self, raw_data):
        raw_data = raw_data['data']['data']
        data = []
        for item in raw_data:
            del item['id']
            del item['comment']
            del item['other']
            data.append(item)
        return data


class HelseDirektoratet_COVID:

    def __init__(self, category=None):
        if category == None:
            self.category = "nasjonalt"
        else:
            self.category = category
        self.url = "api.helsedirektoratet.no/ProduktCovid19/Covid19statistikk/" + self.category
        self.data = []
        self.last_updated = 'NaN'

        self.update()

    def update(self):
        try:
            print("Requesting data from Helsedirektoratet...")
            r = requests.get(url= "https://" + self.url, headers={"Host": "api.helsedirektoratet.no","Ocp-Apim-Subscription-Key":"ba524003671847ee878b5a48528f8675"})
        except requests.exceptions.RequestException as e:
            print(e)
            return
        try:
            raw_data = r.json()
        except json.JSONDecodeError as e:
            print(e)
            print(r.content)
            return
        self.data = self._prepare_data(raw_data)
        time_now = datetime.datetime.now()
        self.last_updated = time_now

    '''
        The Data is already pretty nice from Helsedirektoratet
    '''
    def _prepare_data(self, raw_data):
        data = []
        if self.category == "nasjonalt":
            data = raw_data['registreringer']
        elif self.category == "helseforetak":
            for entry in raw_data:
                if entry["id"] == "0007-0042-St.-Olavs-hospital-":
                    data = entry['covidRegistreringer']
                    break
        else:
            print("Not a valid category, category =", self.category)

        return data


