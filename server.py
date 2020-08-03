from flask import Flask,render_template, url_for, request, session, redirect
from flask_socketio import SocketIO, send, emit
from game import game

app = Flask(__name__)
app.secret_key = 'secret key123'
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
def handleDisconnect():
    global connectedUsers
    connectedUsers -= 1

@socketio.on('victory')
def victory(msg):
    emit("victory", msg,  broadcast=True)

@socketio.on('message')
def handleMessage(msg):
    # message sends which player made a move and to which cell
    player = msg.split()[0]
    cell = msg.split()[1]
    win = 'f'
    #if player wins
    move = game.move(startGame, player, int(cell))
    if(move=="win"):
        win = 't'
        game.reset()
    if(not move=="bad"):
        #broadcast player, move, and if they have won
        send(player+" "+cell+" "+win, broadcast=True)


@app.route("/", methods = ["POST","GET"])
def home():
    if request.method == "POST":
        session["user"] = request.form["name"]
        return redirect(url_for("play"))
    return render_template("home.html")

@app.route("/game")
def play():
    user = session["user"]
    return render_template("game.html", user=user)


if __name__ == "__main__":
    socketio.run(app,debug=True)
