import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
DATABASE = os.path.join(BASE_DIR, 'zhihuscholar.db')

# Secret key for signing cookies
SECRET_KEY = 'secret'
