import os

from flask import redirect, render_template, request, flash, session
from flask_base import app
from datetime import datetime
from flask_base.models.newsletter import News

@app.route("/")
def index():
    nombre_sistema = os.environ.get("NOMBRE_SISTEMA")    
    return render_template("index.html", sistema=nombre_sistema,  all_news=News.get_all_width_picture())

@app.route('/about')
def about():

    return render_template('news/about.html')


@app.route("/contact")
def contact():
    
    nombre_sistema = os.environ.get("NOMBRE_SISTEMA")    
    return render_template("news/contact.html", sistema=nombre_sistema)
