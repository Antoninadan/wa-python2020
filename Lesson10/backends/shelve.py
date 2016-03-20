import shelve
from backends.abstract_backend import AbstractBackend


class ShelveBackend(AbstractBackend):
    def __init__(self):
        super().__init__()
        self.storage = shelve.open('links_db')

    def close(self):
        self.storage.close()
