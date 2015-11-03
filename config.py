import os

class Config(object):
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class DevConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

print(os.environ['DATABASE_URL'])
