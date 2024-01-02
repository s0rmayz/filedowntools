from filedowntools import downloads, ua
import os

# A popular test files for downloading
url1 = 'https://www.python.org/ftp/python/3.5.2/python352.chm.asc'
url2 = 'https://www.python.org/ftp/python/3.7.2/python372.chm.asc'
url3 = 'https://www.python.org/ftp/python/3.9.2/python392.chm.asc'
# A popular User Agent String
user_agent = ua.mac_cha

if __name__ == '__main__':
    headers = {'User-Agent': user_agent}
    files = downloads(url1, url2, url3, headers=headers)
    files.save(os.getcwd())