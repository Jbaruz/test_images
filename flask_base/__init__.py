from flask import Flask
import os
from os. path import join

carpeta = 'uploads'
BASEDIR = os.path.abspath(os.path.dirname(__file__))
UPLOAD_FOLDER = join(BASEDIR, carpeta)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}

app = Flask(__name__)
app.secret_key = os.environ.get("APP_SECRET_KEY")
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER






