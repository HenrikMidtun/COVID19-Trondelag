'''
    Data models:
        load and supply json data
        Call on logger after succesful request
'''

import requests
import dateutil.parser
from datetime import timedelta
from time import localtime, strftime

from logger import CovidLogger

class COVID:
    
    def __init__(self):
        self.url = "spesial.adressa.no/api/covid19trd"
        self.data = {}
        self.last_updated = 'NaN'
        self.logger = CovidLogger()

        self.update_from_log()
        self.update()

    def update(self):
        print("Requesting data from Adressa...")
        
        try:
            r = requests.get(url= "https://" + self.url, headers={"Authorization":"B9329CEF38B2F"})
            raw_data = r.json()

            print("Updating {} data...".format(self.__class__.__name__))
            self.data = self._prepare_data(raw_data)
            iso_time = raw_data['data']['updated']
            last_update = dateutil.parser.isoparse(iso_time)
            self.last_updated = last_update + timedelta(hours=2)

            print("Logging data...")
            self.log_update()

        except:
            print("Something went wrong. Using last logged entry.")
            self.data = self.update_from_log()

    def _prepare_data(self, raw_data):
        raw_data = raw_data['data']['data']
        data = []
        for item in raw_data:
            del item['id']
            del item['comment']
            del item['other']
            data.append(item)
        return data

    def update_from_log(self):
        last_entry = self.logger.get_last_entry()
        self.data = last_entry['data']
        self.last_updated = last_entry['info']['last-update']

    def log_update(self):
        entry = {'info':{'last-update': 'NaN', 'local-time': 'NaN'}, 'data': []}
        last_update = self.last_updated.strftime("%Y-%m-%d %H:%M:%S")
        local_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
        entry['info']['last-update'] = last_update
        entry['info']['local-time'] = local_time
        entry['data'] = self.data
        self.logger.log_data(entry)


        
