from flask import Flask, flash, redirect,render_template,request,session,abort

app = Flask(__name__)

#Mock Data, add other players, find a database?
nba_players = [
    {"name": "LeBron James", "quote": "You can't be afraid to fail. It's the only way you succeed - you're not gonna succeed all the time, and I know that.",
    "img": "https://cloudfront-us-east-1.images.arcpublishing.com/advancelocal/YISHMCH7GZHN7IQPA3PVSV3CDU.jpg"},
    {"name": "Kobe Bryant", "quote": "Everything negative—pressure, challenges—is all an opportunity for me to rise.",
    "img": "https://media.cnn.com/api/v1/images/stellar/prod/200126214640-27-kobe-bryant-gallery-restricted.jpg?q=w_2500,h_2500,x_0,y_0,c_fill"}
]
@app.route("/")
def index():
    return render_template("index.html")

# tester for one player, use random.choice to get random player.
@app.route("/lebron")
def lebron():
    return render_template("template.html",name=nba_players[0]['name'], quote=nba_players[0]['quote'], img=nba_players[0]['img'])

@app.route("/kobe")
def kobe():
    return render_template("template.html",name=nba_players[1]['name'], quote=nba_players[1]['quote'], img=nba_players[1]['img'])


if __name__ == "__main__":
    app.run(debug=True)
