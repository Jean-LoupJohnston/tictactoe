from flask import Flask,render_template, url_for, request, session, redirect
from flask_socketio import SocketIO, send, emit, join_room, leave_room
from game import game

app = Flask(__name__)
app.secret_key = 'secret key123'
socketio = SocketIO(app)
startGame = game()

connectedUsers = 0

@socketio.on('connect')
def handleConnect():
    global connectedUsers
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
    boardNum = msg.split()[2]
    win = 'f'
    #if player wins or draw
    move = game.move(startGame, player, int(cell),int(boardNum))
    #print(startGame.bigBoard)
    #print("move: " + move)

    if(move=="win 10"):
        win = 't 10'
        game.reset(startGame)
    elif(move.split()[0]=="win"):
        win = 't '+move.split()[1]
    elif(move=="draw 10"):
        win = 'd'
        game.reset(startGame)
    if(not move=="bad 10"):
        #broadcast player, move, and if they have won
        send(player+" "+cell+" "+boardNum+" "+win, broadcast=True)


@app.route("/", methods = ["POST","GET"])
def home():
    if request.method == "POST":
        global connectedUsers
        connectedUsers += 1
        session["user"] = request.form["name"]
        return redirect(url_for("play"))
    return render_template("home.html")

@app.route("/game")
def play():
    try:
        user = session["user"]
        return render_template("game.html", user=user)
    except:
        return redirect(url_for("home"))



if __name__ == "__main__":
    socketio.run(app,debug=True)
