import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))
SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(BASE_DIR, 'zhihuscholar.db')
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Secret key for signing cookies
WTF_CSRF_ENABLED = True
SECRET_KEY = 'secret' # Need to be modified in production
