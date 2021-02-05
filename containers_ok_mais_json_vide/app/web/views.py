from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from . import app

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search', methods=['GET', 'POST'])
def search():
    return render_template('search.html')

@app.route('/dataVizualisation')
def dataVizualisation():
    return render_template('dataVizualisation.html')
    