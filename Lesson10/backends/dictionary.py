from backends.abstract_backend import AbstractBackend


class DictionaryBackend(AbstractBackend):
    def __init__(self):
        super().__init__()
        self.storage = {}

