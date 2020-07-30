from flask import Flask,render_template, url_for
from flask_socketio import SocketIO, send
from game import game

app = Flask(__name__)
socketio = SocketIO(app)
startGame = game();

@socketio.on('message')
def handleMessage(msg):
    # message sends which player made and move and to which cell
    player = msg.split()[0]
    cell = msg.split()[1]
    win = 'f'
    #if player wins
    if(game.move(startGame, player, int(cell))):
        win = 't'
        game.reset()
    #broadcast player, move, and if they have won
    send(player+" "+cell+" "+win, broadcast=True)



@app.route("/")
def home():
    return render_template("index.html")


if __name__ == "__main__":
    socketio.run(app,debug=True)
