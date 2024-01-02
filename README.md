# _filedowntools_ library-v0.3.0
#### * __It is used to download files individually or in batches and store them in a specific location.__ 

## Installation
> pip install filedowntools

## Usage
Basic usage: (use __`download()`__ to download small files)
```
>>> from filedowntools import download
>>> image = download('https://www.python.org/static/img/python-logo@2x.png')
>>> image.save('D:\\downloads\\') # Windows
```

When encountering large files, you can use __`large_download()`__:
```
>>> source = large_download('https://www.python.org/ftp/python/3.8.1/python-3.8.1-macosx10.9.pkg')
>>> source.save('D:\\downloads\\')
```

And when you want to download many files, you can use __`downloads()`__:
```
>>> files = downloads(fileurl1, fileurl2, ...)
>>> files.save('D:\\downloads\\')
```

You can get the information with ***`file.stat()`*** too:
```
>>> image.stat()[0] # Status code
200
```

## Contact
### Author: @s0rmayz
### Email: 2430545310@qq.com
