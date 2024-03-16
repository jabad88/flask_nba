from flask import Flask, flash, redirect,render_template,request,session,abort, render_template_string
from flask_sqlalchemy import SQLAlchemy
import os.path
# from db import Player

app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///making_db/players.db'
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
# db = SQLAlchemy(app)


# Mock Data, add other players, find a database?
nba_players = [
    {"name": "LeBron James", "quote": "You can't be afraid to fail. It's the only way you succeed - you're not gonna succeed all the time, and I know that.",
    "img": "https://cloudfront-us-east-1.images.arcpublishing.com/advancelocal/YISHMCH7GZHN7IQPA3PVSV3CDU.jpg"},
    {"name": "Kobe Bryant", "quote": "Everything negative—pressure, challenges—is all an opportunity for me to rise.",
    "img": "https://media.cnn.com/api/v1/images/stellar/prod/200126214640-27-kobe-bryant-gallery-restricted.jpg?q=w_2500,h_2500,x_0,y_0,c_fill"}
]
@app.route("/")
def index():
    return render_template("index.html")

@app.route('/images')
def display_images():
    image_folder = os.path.join(app.static_folder, 'images')
    images = [f for f in os.listdir(image_folder) if os.path.isfile(os.path.join(image_folder, f))]
    return render_template('images.html', images=images)

# @app.route('/players')
# def get_all_players():
#     players = Player.query.all()
#     return "<h1>{{ players }}</h1>"

@app.route("/lebron")
def lebron():
    return render_template("template.html",name=nba_players[0]['name'], quote=nba_players[0]['quote'], img=nba_players[0]['img'])

@app.route("/kobe")
def kobe():
    return render_template("template.html",name=nba_players[1]['name'], quote=nba_players[1]['quote'], img=nba_players[1]['img'])

@app.errorhandler(404)
def page_not_found():
    code = 404
    return f"Page not found. Error Code {code}",404

if __name__ == "__main__":
    app.run(debug=True)


#TODO define route to handle listing all players
#TODO study models
#TODO make another html template 