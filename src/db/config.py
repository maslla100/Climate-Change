import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = False  
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')  # This expects you to set DATABASE_URL in the .env
    DEBUG = False
    TESTING = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_ECHO = True  

class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL')

config = {
    'development': DevelopmentConfig,
    'production': ProductionConfig
}
