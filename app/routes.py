from flask import flash, redirect,render_template,request,session,abort, render_template_string, send_from_directory
from app import app
from app.models import Player
import os

@app.route("/")
def index():
    return render_template("index.html")

@app.route('/images')
def display_images():
    image_folder = os.path.join(app.static_folder, 'images')
    all_files = os.listdir(image_folder)
    file_list = []
    for f in all_files:
        if os.path.isfile(os.path.join(image_folder,f)):
            file_list.append(f)
    return render_template('images.html', images=file_list)

@app.route('/players')
def all_players_list():
    return "<h1>{{ list all players in db through this endpoint }}</h1>"

@app.route("/players/<string:user_id>")
def lebron(user_id):
    lebron = Player.query.get(user_id)
    
    if lebron:
        return render_template("template.html",name=(lebron.first + " "+  lebron.last), quote=lebron.quote)
    else:
        return "Something went wrong finding Lebron"

# @app.route("/kobe")
# def kobe():
#     return render_template("template.html",name=nba_players[1]['name'], quote=nba_players[1]['quote'], img=nba_players[1]['img'])
    

#TODO Get pictures to work for indiviudals players
#Fixed: the players in the database get called from def lebron. Reword this function
#Consider making a frontend for this website.