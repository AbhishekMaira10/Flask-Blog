
import os


class Config:
    # secret keys help protect the forms from modifying cookies, cross-site request forgery attack
    SECRET_KEY = '6fa73538fe5688211055ed30dd556b17'
    #location of thr uri of the database
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'

    # mail server configurations
    MAIL_SERVER = 'smtp.gmail.com'
    MAIL_PORT = 465
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True
    MAIL_USERNAME = os.environ.get('EMAIL_USER')
    MAIL_PASSWORD = os.environ.get('EMAIL_PASS')
