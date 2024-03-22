from flask import render_template,url_for
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
def get_single_player(user_id):
    player = Player.query.get(user_id)
    
    if player:
        get_picture = f"{player.first.lower()}.jpeg"
        
        return render_template("template.html", 
                               name=(player.first + " " +  player.last), 
                               quote=player.quote, 
                               img = url_for('static', filename=f'{get_picture}')
                            )
    else:
        return "Something went wrong finding the NBA player.", 404


#TODO Get pictures to work for indiviudals players
#Fixed: the players in the database get called from def lebron. Reword this function
#Consider making a frontend for this website.