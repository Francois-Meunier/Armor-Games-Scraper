from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from pymongo import MongoClient
from db.tools import init_db, json_to_mongo

app = Flask(__name__)
Bootstrap(app)

client = MongoClient('mongodb_project',27017)

db, collection = init_db('armor_games', collection_name='games_infos') 

json_to_mongo(client, db, collection)

from web import views