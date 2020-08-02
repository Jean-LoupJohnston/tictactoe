from flask import Flask,render_template, url_for
from flask_socketio import SocketIO, send, emit
from game import game

app = Flask(__name__)
app.secret_key = 'secret key'
socketio = SocketIO(app)
startGame = game()

connectedUsers = 0


@socketio.on('connect')
def handleConnect():
    global connectedUsers
    connectedUsers += 1
    if(connectedUsers==1):
        emit("connect", "X")
    else:
        emit("connect", "O" )

@socketio.on('disconnect')
def handleConnect():
    global connectedUsers
    connectedUsers -= 1

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
