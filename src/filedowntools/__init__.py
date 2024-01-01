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

""" 

from .download import *

__version__ = '0.2.1'