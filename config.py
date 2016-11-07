import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hard to guess string'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    BLOGY_MAIL_SUBJECT_PREFIX = '[Blogy]'
    BLOGY_MAIL_SENDER = 'Chen Liang <chenliang@3tcloud.com>'
    BLOGY_ADMIN = 'chenliang@3tcloud.com'

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.3tcloud.com'
    MAIL_USERNAME = 'chenliang'
    MAIL_PASSWORD = 'wzxhn@0926'
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:19810926@localhost/test'


config = {
    'development': DevelopmentConfig,

    'default': DevelopmentConfig
}
