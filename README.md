# Table of contents

<!-- TOC -->
- [Table of contents](#table-of-contents)
- [Presentation](#Presentation)
- [Needed tools](#Needed-tools)
  - [Git](#git)
  - [Docker](#docker)
- [Launch the app](#Launch-the-app)
- [Issues](#Issues)
- [Dev guide](#De-guide)
  - [Scrap](#Scrap)
  - [App](#App)
- [Help](#help)
- [Credits](#credits)

# Presentation

**Armor Games Scraper** is an app that can be used to search more precisely for flash games on armor games. We wante to create this because when I was a kid, I used a lot armor games website to pplay flash games.
But now when i want to look for a game that I played before the website tools for searching games is a bit crappy, like without date search or year search only name.

This web app was created for a course, in our school **ESIEE PARIS**, named **Data Engineering** it is using:<br/>
**Scrap**, a python package used to get data on choosen web page.<br/>
**Flask**, a python framework made to easily create back-end with python.<br/>
**Bootstrap**, a python tools kit that is used to develop front-end in python.<br/>
**MongoDB**, a database technologie that we used to save all our scrap informations about each game

We were three on this project:<br/>
[Lorenzo PINAUD](https://www.linkedin.com/in/lorenzo-pinaud-10a8601b7/)<br/>
[Francois MEUNIER](https://www.linkedin.com/in/fran%C3%A7ois-meunier-981194172/)<br/>
[jules CHEVENET](https://www.linkedin.com/in/jules-chevenet-4441b4189/)

# Needed tools

## Git 

You first need to download the directory, with two possibilities:

1.If you are used to Git, just used:

```
$ git clone https://github.com/Francois-Meunier/Armor-Games-Scraper.git 
```
2.If you don't know how to do it with command you can just download with the **Code/Download ZIP**

## Docker

Docker is a tool designed to make it easier to create, deploy, and run applications by using containers. Containers allow a developer to package up an application with all of the parts it needs, such as libraries and other dependencies, and ship it all out as one package

You can download Docker and Docker Compose by following this [Docker install page](https://www.docker.com/get-started)

You will have to install **Docker** and **Docker Compose** to make the app work

# Launch the app

You need **Docker** and **Docker Compose** to run the app, follow this feww steps:

1.Open your shell and move to the project directory
2.Launch the docker container with the command:
```bash
$ docker-compose up
```
3.Then check if you got this output:

Mettre la réponse de cmd pour la réussite de l'installation de docker

4.The final step, noww that the app is running is to onto it:
                [Armor games scraper](http://0.0.0.0:5000/)
                


If you want to update the json files to change the database, you will need to go in python prompt and move to armor_games_crawler(don't forget to delete the json files to not write again on the same files and create a glitch wwwhen you will launch the app)
```
move newscrawler\spiders\spyder_games_infos.py temporaire 
scrapy crawl url_scrapper -o data/jeux_urls.json
move temporaire\spyder_games_infos.py newscrawler\spiders
scrapy crawl jeux_infos_scrapper -o data/jeux_infos.json
```


# Issues

We had many issues while creating this project, the first one was that the scrap cannot pput the data scraped in the json and mongo database while using pipelines. That's wwhy we decided to separe it to make the scrap by command.
The other problem that was intern to the scrap was that even manually, it cannot crawl while both spyder are in the spider files, that is why we are moving the second spider before crawl the link. The problem is that even if we only crawl the first spider, the second will still verify if it could work, problem at the begining of the second spider we are loading the json files that we created with the first spider.

# Dev guide

A guide to explain how the different part is working

## Scrap 

For the scrap we are using scrapy and crawler, a crawler is very usefull while the setting and pipelines are really practical to process the data that is scraped.
We got one pipelines for each item, like that we can change the date to be able to use to in the search page of the app.

pipelines.py:

NamePipeline = used to clean the space at the end of each name. 
PublishedPipeline = used to change the date format using a dict created to change the month in number.
RatingsPipeline = used to change the rating, by cleaning the comma.
FavoritesPipeline = used to change the number of time the game was define as favorite, by cleaning the comma.
PlaysPipeline = used to change the number of times the game was played, by cleaning the comma.
MongoPipeline = was created to load the data in the mongodb but was canceled, while it didn't work.


clean_comma = function to clear comma.
clean_space = function to clear space.

The files items.py:
Games_Infos_Item = item used in the second crawler to get all the infos such as tags, description etc...
Games_Link_Item = item used for the first crawler used to get the link of each game and the pictures of each game.

finaly settings.py:

USER_AGENTS = used to change the user agent while scraping.
DOWNLOADER_MIDDLEWARES = to define the parameters of user agent change.

To improve the number of data scraped, we were trying to use proxy change, but the implementation didn't change a thing.
So on the 1400 games on the site only 400 were scraped,even while changing the download delay we were still having issues with 429 error(when a site limits your connection, to prevent  ddos or mass attack.

## App

The app is in two pages:

The first one is used to search for games using name date.
The second is graphic analyse, on the games, such as ratings by plays, or ratings by tag.

# Help

If you have any issues with the app, or you just want informations on the documentation, ask one of us.

# Credits

We would like to thanks our three teachers, to pass their knownledg and for the help they gave in this project:
- **COURIVAUD Raphaël**
- **KOUEK Jean-Baptiste**
- **BERCHER Jean-François**
