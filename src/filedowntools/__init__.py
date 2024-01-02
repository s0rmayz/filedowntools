"""
filedowntools library
~~~~~~~~~~~~~~~~~~~~~~

It is used to download files individually or in batches and store them in a specific location.
Basic usage:
    >>> from filedowntools import download
    >>> image = download('https://www.python.org/static/img/python-logo@2x.png')
    >>> image.save('D:\\downloads\\') # Windows

When encountering large files, you can use large_download():
    >>> source = large_download('https://www.python.org/ftp/python/3.8.1/python-3.8.1-macosx10.9.pkg')
    >>> source.save('D:\\downloads\\')

And when you want to download many files, you can use downloads():
    >>> files = downloads(fileurl1, fileurl2, ...)
    >>> files.save('D:\\downloads\\')

You can get the information too:
    >>> image.stat()[0]
    200

You can also use the sample User Agents in headers: (use ua())
    >>> from filedowntools import ua
    >>> my_ua = ua.mac_cha
    >>> my_ua
    Mozilla/5.0(Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML like Gecko) Chrome/109.0.0.0 Safari/537.36
    >>> image = download('https://www.python.org/static/img/python-logo@2x.png', 
            headers={'User-Agent': my_ua})
    >>> image.save('D:\\downloads\\')

""" 

from .download import *
from .user_agents import *

__all__ = ['download', 'large_download', 'downloads', 'ua']

__version__ = '0.5.1'