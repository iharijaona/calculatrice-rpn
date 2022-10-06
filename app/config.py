"""Configuration file."""

from os import environ, path

class Config(object):
    """Config class."""

    #: Flask app name.
    APP_NAME = 'RPN Api'

    APP_DESC = 'REST API for RPN calculation.'
    
    #: development or production
    FLASK_ENV = environ.get('FLASK_ENV', 'development')

    TESTING = True if environ.get('TESTING') == 'True' else False

    #: DEBUG flag.
    DEBUG = True if environ.get('DEBUG') == 'True' else False

    #: Flask app port
    APP_PORT = int(environ.get('APP_PORT', 8888))

    #: Flask app secret key.
    SECRET_KEY = environ.get('SECRET_KEY', '4e0ea1bb-6702-4e74-a514-bc12bcd4810e')

    #: Supported operands
    OPERAND_LIST = ['+', '-', '*', 'div']