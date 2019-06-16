from app import create_app 
from app.models import User , Measurement ,db , Metadata
import os
import logging
from logging.handlers import RotatingFileHandler
from flask import current_app

app = create_app()

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User , 'Measurement': Measurement , 'Metadata': Metadata }
