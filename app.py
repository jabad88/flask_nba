from flask import Flask, flash, redirect,render_template,request,session,abort
app = Flask(__name__)

#Mock Data, add other players, find a database?
nba_players = [
    {"name": "LeBron James", "quote": "You can't be afraid to fail. It's the only way you succeed - you're not gonna succeed all the time, and I know that.",
    "img": "https://cloudfront-us-east-1.images.arcpublishing.com/advancelocal/YISHMCH7GZHN7IQPA3PVSV3CDU.jpg"},
]
@app.route("/")
def index():
    return "Welcome to the website. Get a quote from your favorite NBA players"

# tester for one player, use random.choice to get random player.
@app.route("/lebron")
def lebron():
    return render_template("template.html",name=nba_players[0]['name'], quote=nba_players[0]['quote'], img=nba_players[0]['img'])

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
