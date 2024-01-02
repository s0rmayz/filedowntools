from filedowntools import large_download, ua
import os

# A popular test file for large-downloading
url = 'https://www.python.org/ftp/python/2.7.18/python2718.chm.asc'
# A popular User Agent String
user_agent = ua.mac_cha

if __name__ == '__main__':
    headers = {'User-Agent': user_agent}
    file = large_download(url, headers=headers)
    file.save(os.getcwd())