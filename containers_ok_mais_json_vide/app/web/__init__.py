from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
from db.tools import init_db, feed_db_json

app = Flask(__name__)
Bootstrap(app)

from . import views


# Init MongoDB
database, collection = init_db('armor_games', collection_name='games_infos')

try:
    # Feed MongoDB from the webscraping
    filename = 'jeux_infos.json'
    feed_db_json(filename, collection=collection)
except:
    pass
