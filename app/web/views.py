from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask import Response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import pandas as pd
import io
import numpy as np
import matplotlib.pyplot as plt
from . import app
from . import db, collection

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

def plot_data(cursor,twoCat,color):
    all_list = []
    for name in twoCat:
        all_list.append([])
    for el in cursor :
        for i in range(len(all_list)) :
            all_list[i].append(el[twoCat[i]])
    a = np.array(all_list)
    f = plt.figure()
    axarr = f.add_subplot(1,1,1)
    plt.scatter(a[0],a[1],c=color,marker = 'x',alpha = 0.4)
    plt.ylabel('Numbers of '+twoCat[0]+'')
    plt.xlabel('Numbers of ' + twoCat[1]+'')
    plt.yscale('log')
    plt.grid(True)
    return(f)


col_list = ["name","plays","favorites","ratings","lien","image"]

plays = data_top(collection.find().sort([("plays",-1)]).limit(15), col_list)

fav = data_top(collection.find().sort([("favorites",-1)]).limit(15), col_list)

ratings = data_top(collection.find().sort([("ratings",-1)]).limit(15), col_list)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/plot.png')
def plot_png():
    fig = plot_data(collection.find(),['favorites','plays'], 'red')
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/plot2.png')
def plot2_png():
    fig = plot_data(collection.find(),['ratings','plays'], 'blue')
    output = io.BytesIO()
    FigureCanvas(fig).print_png(output)
    return Response(output.getvalue(), mimetype='image/png')


@app.route('/totalStats', methods=("POST", "GET"))
def totalStats():

    return render_template('totalStats.html',  tables=[plays.to_html(classes='plays'), ratings.to_html(classes='ratings'), fav.to_html(classes='fav')])


@app.route('/dataVizualisation')
def dataVizualisation():
    return render_template('dataVizualisation.html')