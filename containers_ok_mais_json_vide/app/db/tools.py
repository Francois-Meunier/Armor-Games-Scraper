
from pymongo import MongoClient
import json

#variable for the mongo client
MONGODB = 'mongodb_project'
PORT = 27017

#dictionnaire pour les mois
Mois_nombre = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04",
              "May" : "05", "Jun" : "06", "Jul" : "07", "Aug" : "08",
              "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12"}

#funstion to clean the json items
def clean_comma(string):
        if "," in string:
            return string.replace(",","")
        else:
            return string

def clean_space(string):
    if " " in string:
        return "0"+string.replace(" ","")
    else:
        return string


def init_db(db_name, collection_name=None):
    
    # Initiate the MongoClient with the variables define top
    client = MongoClient(MONGODB, PORT)

    # Get the database named with the db_name value
    database = client[db_name]

    # If given, get the corresponding collection
    if collection_name:
        collection = database[collection_name]

        return database, collection

    # Just return the database otherwise
    return database

def feed_db_json(filepath, collection):
    """to import a json file in the database"""


    i = 0
    with open(filepath) as f:
        items = json.load(f)

    # loop to get all the item
    for item in items['items']:
        try:

            # Process the tags
            item["published"] = clean_comma(item["published"])
            item["published"] = clean_space(item["published"][4:6])+"/"+Mois_nombre.get(item["published"][0:3])+"/"+item["published"][7:11]

            item["ratings"] = clean_comma(item["ratings"])

            item["favorites"] = clean_comma(item["favorites"])

            item["plays"] = clean_comma(item["plays"])

            item["name"] = item["name"][:-1]

            # Insert the item in the collection
            collection.insert_one(item)
            i += 1
        except:
            pass

    print(f'> {i} items were transfered in the database.')
    print(f"> {len(items['items']) - i} items were not transfered in the database.")