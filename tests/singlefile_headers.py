from filedowntools import download, ua
import os

# A popular test file for downloading
url = 'https://www.python.org/static/img/python-logo@2x.png'
# A popular User Agent String
user_agent = ua.mac_cha

if __name__ == '__main__':
    headers = {'User-Agent': user_agent}
    image = download(url, headers=headers)
    image.save(os.getcwd())