"""
download
~~~~~~~~
Download a file or files.
"""

import functools
import requests
import os.path
from .errors import *

def _raise_error(*args):
    raise DownloadError(*args) from None

def _except_exceptions(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            return result
        except requests.exceptions.RequestException as e:
            _raise_error(e.args[0])
    return wrapper

def _split(file: str):
    return file.split('?')[0]

class download:
    """Download a small file."""
    @_except_exceptions
    def __init__(self, url):
        self.res = requests.get(url)
        self.filename = os.path.split(url)[1]

    @_except_exceptions
    def save(self, location):
        with open(os.path.join(location, _split(self.filename)), 'wb') as f:
            f.write(self.res.content)

    @_except_exceptions
    def stat(self):
        return self.res.status_code, self.res.headers, 

class large_download(download):
    """Download large files in chunks."""
    @_except_exceptions
    def __init__(self, url):
        self.res = requests.get(url, stream=True)
        self.filename = os.path.split(url)[1]

    @_except_exceptions
    def save(self, location):
        with open(os.path.join(location, _split(self.filename)), 'wb') as f:
            for chunk in self.res.iter_content(chunk_size=1024):
                if chunk:
                    f.write(chunk)

class downloads(download):
    """Download files."""
    @_except_exceptions
    def __init__(self, *urls):
        self.resources = [requests.get(res) for res in urls]
        self.filenames = [os.path.split(url)[1] for url in urls]

    @_except_exceptions
    def save(self, location):
        for index, res in enumerate(self.resources):
            with open(os.path.join(location, _split(self.filenames[index])), 'wb') as f:
                f.write(res.content)