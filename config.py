import os

class Config:
    SECRET_KEY = os.urandom(24)
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''  # Add your MySQL password if required
    MYSQL_DB = 'obituary_platform'
    MYSQL_CURSORCLASS = 'DictCursor'
