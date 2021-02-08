from flask import Flask, render_template, request
from flask_bootstrap import Bootstrap
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure

import pandas as pd
import io
import numpy as np
import matplotlib.pyplot as plt
import plotly
import plotly.graph_objs as go
import plotly.express as px
import json

from . import app
from . import db, collection


# fonctions
def data_top(cursor, listeCol):
    columns = {name : [] for name in listeCol}
    df_top = pd.DataFrame(columns, columns = listeCol)
    all_list = []
    for name in listeCol:
        all_list.append([])
    for i in range(len(listeCol)):
        df_top[listeCol[i]] = all_list[i]
    for el in cursor :
        for i in range(len(all_list)) :
            all_list[i].append(el[listeCol[i]])
    for i in range(len(listeCol)) :
        df_top[listeCol[i]] = all_list[i]
    return df_top

def data_plot(cursor, ThreeCol):
    columns = {name : [] for name in ThreeCol}
    df = pd.DataFrame(columns, columns = ThreeCol)
    all_list = []
    for name in ThreeCol:
        all_list.append([])
    for i in range(len(ThreeCol)):
        df[ThreeCol[i]] = all_list[i]
    for el in cursor :
        for i in range(len(all_list)) :
            all_list[i].append(el[ThreeCol[i]])
    for i in range(len(ThreeCol)) :
        df[ThreeCol[i]] = all_list[i]

    fig = [go.Scatter(x=df[ThreeCol[0]], y =df[ThreeCol[1]], mode = 'markers', text=df[ThreeCol[2]])]

    graphJSON = json.dumps(fig, cls=plotly.utils.PlotlyJSONEncoder)

    return graphJSON

# creation d'un indeex pour recherche par nom
collection.create_index([("name",  "text")])

col_list = ["name","plays","favorites","rating","link","picture"]

plays = data_top(collection.find().sort([("plays",-1)]).limit(15), col_list)

fav = data_top(collection.find().sort([("favorites",-1)]).limit(15), col_list)

rating = data_top(collection.find().sort([("rating",-1)]).limit(15), col_list)

# variables pour les graphs
ThreeCol1 = ['plays',"favorites",'name']
ThreeCol2 = ['plays',"rating",'name']

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/search')
def form():
    return render_template('search.html')


@app.route('/search', methods=['POST'])
def search():
    text = request.form['u']
    processed_text = text.upper()
    cur = collection.find( { "$text": { "$search": processed_text } } )
    search = data_top(cur, col_list)
    return render_template('searchResult.html',  tables=[search.to_html(classes='search')])


@app.route('/totalStats', methods=("POST", "GET"))
def totalStats():

    return render_template('totalStats.html',  tables=[plays.to_html(classes='plays'), rating.to_html(classes='rating'), fav.to_html(classes='fav')])


@app.route('/dataVizualisation')
def dataVizualisation():
    cursor = collection.find()
    scatter1 = data_plot(cursor,ThreeCol1)
    cursor2 = collection.find()
    scatter2 = data_plot(cursor2,ThreeCol2)
    return render_template('dataVizualisation.html', plot = scatter1, plot2 = scatter2)