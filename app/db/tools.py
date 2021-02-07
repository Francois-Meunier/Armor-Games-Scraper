from pymongo import MongoClient
import json
import pandas as pd
import pymongo

def init_db(db_name, collection_name=None):
    
    # Initiate the MongoClient with the variables define top
    client = MongoClient('mongodb_project', 27017)

    # Get the database named with the db_name value
    database = client[db_name]

    # If given, get the corresponding collection
    if collection_name:
        collection = database[collection_name]

        return database, collection

    # Return db
    return database

def json_to_mongo(client, db, collection) :
    df = pd.read_json(r'armorgamescrawler/data/jeux_infos.json')
    dict_jeux = df.to_dict('records')
    collection.insert_many(dict_jeux)
    return ()

### maybe useless now ###

# # dictionnaire pour les mois
# Mois_nombre = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04",
#               "May" : "05", "Jun" : "06", "Jul" : "07", "Aug" : "08",
#               "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12"}

# # function to clean the json items
# def clean_comma(string):
#         if "," in string:
#             return string.replace(",","")
#         else:
#             return string

# def clean_space(string):
#     if " " in string:
#         return "0"+string.replace(" ","")
#     else:
#         return string