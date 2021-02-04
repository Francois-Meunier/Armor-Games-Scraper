# Table of contents

<!-- TOC -->
- [Table of contents](#table-of-contents)
- [Presentation](#Presentation)
- [Needed tools](#Needed-tools)
  - [Git](#git)
  - [Docker](#docker)
- [Launch the app](#Launch-the-app)
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

We were three on this project:
[Lorenzo PINAUD](https://www.linkedin.com/in/lorenzo-pinaud-10a8601b7/)
[Francois MEUNIER](https://www.linkedin.com/in/fran%C3%A7ois-meunier-981194172/)
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


1. Navigate your shell into the project directory
2. Launch the following command
```bash
$ docker-compose up
```
3.Then check if you got this output:

Mettre la réponse de cmd pour la réussite de l'installation de docker

4.The final step, noww that the app is running is to onto it:
                [Armor games scraper](http://0.0.0.0:5000/)
# Help

If you have any issues with the app, or you just want informations on the documentation, ask one of us.

# Credits

We would like to thanks our three teachers, to pass their knownledg and for the help they gave in this project:<br/>
- **COURIVAUD Raphaël**<br/>
- **KOUEK Jean-Baptiste**<b/>
- **BERCHER Jean-François**
