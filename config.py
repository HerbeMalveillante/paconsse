import os
from dotenv import load_dotenv

load_dotenv()

class Config(object):
    VERSION = '0.0.1'
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
