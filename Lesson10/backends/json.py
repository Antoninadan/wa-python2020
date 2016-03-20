import json
from backends.abstract_backend import AbstractBackend

FILENAME = 'links_db.json'


class JSONBackend(AbstractBackend):
    def __init__(self):
        super().__init__()
        self._load_data()

    def _load_data(self):
        with open(FILENAME) as file:
            self.storage = json.load(file)

    def close(self):
        with open(FILENAME, 'w') as file:
            json.dump(self.storage, file, indent=2)
