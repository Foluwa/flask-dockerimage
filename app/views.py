from flask import render_template

from app import app

@app.route('/')
def home():
   return "<strong>Welcone to this docker image</strong>"

@app.route('/template')
def template():
    return render_template('home.html')
