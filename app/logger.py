import jsonlines
import os.path
from model import COVID
from time import localtime, strftime


class CovidLogger:
    def __init__(self):
        self.covid = COVID()
        self.log_path = 'history.jsonl'
        if not os.path.isfile(self.log_path):
            f = open(self.log_path, 'w')

    def log_data(self, data):
        with jsonlines.open(self.log_path, mode='a') as writer:
            writer.write(data)

    def get_log(self):
        log_data = []
        with jsonlines.open(self.log_path) as reader:
            for obj in reader.iter():
                log_data.append(obj)
        return log_data

    def get_last_entry(self):
        log = self.get_log()
        if len(log) == 0:
            return None
        return log[-1]
    
    def update(self, data):
        log_data(data)

    def log_update(self):
        entry = {'info':{'last-update': 'NaN', 'local-time': 'NaN'}, 'data': []}
        last_update = self.covid.last_updated.strftime("%Y-%m-%d %H:%M:%S")
        local_time = strftime("%Y-%m-%d %H:%M:%S", localtime())
        entry['info']['last-update'] = last_update
        entry['info']['local-time'] = local_time
        entry['data'] = self.covid.data

        

