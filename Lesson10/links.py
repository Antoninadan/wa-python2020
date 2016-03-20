class LinkStorage:
    def __init__(self, backend):
        self.backend = backend

    def add_link(self, short_name, url):
        if short_name in self.backend.storage:
            raise KeyError('link already exists')
        self.backend.storage[short_name] = url

    def get_link(self, short_name):
        return self.backend.storage[short_name]

    def remove_link(self, short_name):
        del self.backend.storage[short_name]

    def close(self):
        self.backend.close()
