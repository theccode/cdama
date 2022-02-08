import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    MAIL_SERVER = os.environ.get('MAIL_SERVER', 'smtp.google.com')
    MAIL_PORT = os.environ.get('MAIL_PORT', '587')
    MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS', 'true').lower() in ['true', 'on', '1']
    MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
    MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
    CDAMA_MAIL_SUBJECT_PREFIX = 'CDAMA'
    CDAMA_MAIL_SENDER = 'CDAMA Admin <cdamaadmin@gmail.com'
    CDAMA_ADMIN = os.environ.get('CDAMA_ADMIN')
    SQL_ALCHEMY_TRACK_MODIFICATIONS = False

class DevelopmentConfig(Config):
    DEBUG = True
    SQL_ALCHEMY_DATABASE_URI = os.environ.get('DEVELOPMENT_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')

class TestingConfig(Config):
    DEBUG = True
    SQL_ALCHEMY_DATABASE_URI = os.environ.get('TESTING_URI') or \
        'sqlite:///'

class ProductionConfig(Config):
    DEBUG = True
    SQL_ALCHEMY_DATABASE_URI = os.environ.get('PRODUCTION_URI') or \
        'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}