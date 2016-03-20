import shelve

_links = None


def add_link(short_name, url):
    if short_name in _links:
        raise KeyError('link already exists')
    _links[short_name] = url


def get_link(short_name):
    return _links[short_name]


def remove_link(short_name):
    del _links[short_name]


def initialize():
    global _links
    _links = shelve.open('links_db')


def finalize():
    _links.close()
