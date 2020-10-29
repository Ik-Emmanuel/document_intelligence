from flask import Flask
from config import Config
from flask_mongoengine import MongoEngine
from flask_restplus import Resource, Api
import urllib.request
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
import requests
import json
from IPython.display import display, HTML
import urllib
import importlib
import time
import getopt
import sys
from requests import get, post
from pathlib import Path

# api = Api()

app = Flask(__name__)
app.config.from_object(Config)




db = MongoEngine()
db.init_app(app)
# api.init_app(app)


UPLOAD_FOLDER = "C:/Users/Nwokochaui/Desktop/IPYTHONNOTEBOOKS/2020 Applied Machine Learning/2020 sterling work projects/Contact Intelligence/mslearn-build-ai-web-app-with-python-and-flask-master/src/starter/whole new worlds  for messing up/static/pdf/"

 

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
 
ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif', 'docx'])
 
def allowed_file(filename):
 return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


from application import routes





if __name__=="__main__":
    app.run( debug=True) 