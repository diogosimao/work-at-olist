import os
import environ
from neattree.settings import *

root = environ.Path(__file__) - 4
env = environ.Env(DEBUG=(bool, False),)

# read the .env file associated with the settings that're loaded
env.read_env()

BASE_DIR = root()

SECRET_KEY = env('SECRET_KEY')

INSTALLED_APPS.append('django_generate_secret_key',)

secret_key_file_path = os.path.join(BASE_DIR, 'secretkey.txt')
if os.path.exists(secret_key_file_path):
    with open(secret_key_file_path) as f:
        SECRET_KEY = f.read().strip()

DEBUG = env('DEBUG')

DATABASES = {
    'default': env.db(),
}
