from scrapy.exceptions import DropItem
import pymongo


#dictionnaire pour les mois
Mois_nombre = {"Jan" : "01", "Feb" : "02", "Mar" : "03", "Apr" : "04",
              "May" : "05", "Jun" : "06", "Jul" : "07", "Aug" : "08",
              "Sep" : "09", "Oct" : "10", "Nov" : "11", "Dec" : "12"}

class NamePipeline():

    #enlever les espace des dates et noms du au scrap
    def process_item(self, item, spider):
        if item["name"]:
            item["name"] = item["name"][:-1]
            return item
        else:
            raise DropItem("Missing date or name in %s" % item)

class PublishedPipeline():

    #enlever les espace des dates et noms du au scrap
    def process_item(self, item, spider):

        if item['published']:
            item["published"] = clean_comma(item["published"])
            item["published"] = clean_space(item["published"][4:6])+"/"+Mois_nombre.get(item["published"][0:3])+"/"+item["published"][7:11]
            return item
        else:
            raise DropItem("Missing date or name in %s" % item)

            

class RatingsPipeline():

    #enlever les virgules de ratings pour pas que mongo prenne ca pour des double
    def process_item(self, item, spider):
        if item["rating"]:
            item["rating"] = clean_comma(item["rating"])
            return item
        else:
            raise DropItem("Missing number")  

class FavoritesPipeline():

    #enlever les virgules de favorites pour pas que mongo prenne ca pour des double
    def process_item(self, item, spider):
        if item["favorites"]:
            item["favorites"] = clean_comma(item["favorites"])
            return item
        else:
            raise DropItem("Missing number")

class PlaysPipeline():

    #enlever les virgules de plays pour pas que mongo prenne ca pour des double
    def process_item(self, item, spider):
        if item["plays"]:
            item["plays"] = clean_comma(item["plays"])
            return item
        else:
            raise DropItem("Missing number")
    
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

#partie automatisation avec mongo

class MongoPipeline():

    collection_name = 'armor_games_infos'

    def open_spider(self, spider):
        self.client = pymongo.MongoClient("mongodb://127.0.0.1:27017")
        self.db = self.client["jeux_infos_scrapper"]
        try:
            self.db[self.collection_name].drop()#suppresion de la collection pour quand on relance le scrap.
        except:
            pass
        
    def close_spider(self, spider):
        self.client.close()

    def process_item(self, item, spider):
        self.db[self.collection_name].insert_one(dict(item))
        return item