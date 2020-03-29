'''
    Data models:
        load and supply json data
'''

import requests
import dateutil.parser

class COVID:
    
    def __init__(self):
        self.url = "spesial.adressa.no/api/covid19trd"
        self.data = {}
        self.last_updated = 'NaN' #kanskje det finnes noe bedre null verdi
        
        self.update()

    
    def update(self):
        print("Requesting data from Adressa...")
        r = requests.get(url= "https://" + self.url, headers={"Authorization":"B9329CEF38B2F"})
        f_json = r.json()
        
        print("Updating {} data...".format(self.__class__.__name__))
        self.data = f_json['data']['data']
        
        iso_time = f_json['data']['updated']
        last_update = dateutil.parser.isoparse(iso_time)
        self.last_updated = last_update

        