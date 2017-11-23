import os
import environ
from neattree.settings import *

root = environ.Path(__file__) - 4
env = environ.Env(DEBUG=(bool, False),)

# read the .env file associated with the settings that're loaded
env.read_env()

BASE_DIR = root()

INSTALLED_APPS.append('django_generate_secret_key',)

with open(os.path.join(BASE_DIR, 'secretkey.txt')) as f:
    SECRET_KEY = f.read().strip()

DEBUG = env('DEBUG')

DATABASES = {
    'default': env.db(),
}
