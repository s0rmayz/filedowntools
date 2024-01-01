"""
errors
~~~~~~
Override network exceptions.
"""

class NetException(Exception):
    pass

class DownloadError(NetException):
    pass