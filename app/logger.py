import jsonlines

class CovidLogger:
    def __init__(self):
        self.log_path = 'history.jsonl'

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
        return log[-1]
    
    def update(self, data):
        log_data(data)

    

        

