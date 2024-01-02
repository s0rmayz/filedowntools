from filedowntools import large_download
import os

# A popular test file for large-downloading
url = 'https://www.python.org/ftp/python/2.7.18/python2718.chm'

if __name__ == '__main__':
    file = large_download(url)
    file.save(os.getcwd())