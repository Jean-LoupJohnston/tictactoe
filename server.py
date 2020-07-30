from flask import Flask,render_template, url_for
from game import game

app = Flask(__name__)

c0 = game.board[0][0]
c1 = game.board[0][1]
c2 = game.board[0][2]
c3 = game.board[1][0]
c4 = game.board[1][1]
c5 = game.board[1][2]
c6 = game.board[2][0]
c7 = game.board[2][1]
c8 = game.board[2][2]


@app.route("/")
def home():
    return render_template("index.html",c0=c0,c1=c1,c2=c2,c3=c3,c4=c4,c5=c5,
                           c6=c6,c7=c7,c8=c8)
    
    
if __name__ == "__main__":
    app.run(debug=True)
