from filedowntools import downloads
import os

# A popular test files for downloading
url1 = 'https://www.python.org/ftp/python/3.5.2/python352.chm'
url2 = 'https://www.python.org/ftp/python/3.7.2/python372.chm'
url3 = 'https://www.python.org/ftp/python/3.9.2/python392.chm'

if __name__ == '__main__':
    files = downloads(url1, url2, url3)
    files.save(os.getcwd())