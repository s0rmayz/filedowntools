from filedowntools import download
import os

# A popular test file for downloading
url = 'https://www.python.org/static/img/python-logo@2x.png'

if __name__ == '__main__':
    image = download(url)
    image.save(os.getcwd())