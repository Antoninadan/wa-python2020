_links = {}


def add_link(short_name, url):
    if _links.get(short_name) is not None:
        raise KeyError('link already exists')
    _links[short_name] = url


def get_link(short_name):
    return _links[short_name]
