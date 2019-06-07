import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'djvdskjfkfjlknfbuhdf'

    # SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'postgres+psycopg2://postgres:azerty1@localhost:5432/HSTS' 

    SQLALCHEMY_DATABASE_URI = 'postgres+psycopg2://postgres:root@toor@localhost:5432/HomeDB' 
    
    SQLALCHEMY_TRACK_MODIFICATIONS = False
