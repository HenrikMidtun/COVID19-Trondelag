'''
    Data models:
        load and supply json data
'''

import requests
import dateutil.parser
from datetime import timedelta

class COVID:
    
    def __init__(self):
        self.url = "spesial.adressa.no/api/covid19trd"
        self.data = {}
        self.last_updated = 'NaN'

        self.update()

    def update(self):
        print("Requesting data from Adressa...")
        try:
            r = requests.get(url= "https://" + self.url, headers={"Authorization":"B9329CEF38B2F"})
        except requests.exceptions.RequestException as e:
            print(e)
            r = None
        if r != None:
            raw_data = r.json()
            print("Updating {} data...".format(self.__class__.__name__))
            self.data = self._prepare_data(raw_data)
            iso_time = raw_data['data']['updated']
            last_update = dateutil.parser.isoparse(iso_time)
            self.last_updated = last_update + timedelta(hours=1)

    def _prepare_data(self, raw_data):
        raw_data = raw_data['data']['data']
        data = []
        for item in raw_data:
            del item['id']
            del item['comment']
            del item['other']
            data.append(item)
        return data




        
