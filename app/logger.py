import jsonlines


class CovidLogger:
    def __init__(self):
        self.log_path = 'history.jsonl'

    def log_data(self, data):
        with jsonlines.open(self.log_path, mode='a') as writer:
            writer.write(data)

    def _get_last_entry(self):
        with jsonlines.open(self.log_path) as reader:
            for obj in reader.iter():
                print(reader.read())

logger = CovidLogger()
#logger.log_data({"hei":"verden"})
logger._get_last_entry()

