import os
import environ
from neattree.settings import *

root = environ.Path(__file__) - 4
env = environ.Env(DEBUG=(bool, False),)

env.read_env()

BASE_DIR = root()

SECRET_KEY = env('SECRET_KEY')

DEBUG = env('DEBUG')

DATABASES = {
    'default': env.db(),
}
