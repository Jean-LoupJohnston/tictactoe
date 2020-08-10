import os
import random

from flask import Flask,render_template, url_for, request, session, redirect
from flask_socketio import SocketIO, send, emit, join_room, close_room
from game import game


app = Flask(__name__)
app.secret_key = os.environ.get('SECRET')
SocketIO(app,cors_allowed_origins="*")
socketio = SocketIO(app)
gameBoards = {}
userPairs = {}

@socketio.on('connect')
def handleConnect():
#assign either "X" or "O" to user based on placement in dict
#every user joins a room on their own

    join_room(session["user"])
    opponent = ""
    for x, y in userPairs.items():
        if x == session["user"]:
            opponent = y
            break
        if y == session["user"]:
            opponent = x
            break

    for x, y in userPairs.items():
        if y == session["user"]:
            emit("connect", "X "+ session["user"], room = opponent)
            emit("connect", "O "+ opponent, room = session["user"])
            break
    print(userPairs)

#if user disconnects, close their room, take them out of userPairs
#delete their gameboard
#tell other player their opponent left
@socketio.on('disconnect')
def handleDisconnect():
    try:
        close_room(session["user"])
        del gameBoards[session["user"]]
    except Exception as e:
        print(e)
    for x, y in userPairs.items():
        if x == session["user"]:
            emit("disconnect", y, room = y)
            if(y):
                gameBoards[y] = game()
            if(userPairs[x]):
                userPairs[y] = False;
                del userPairs[x]
                break
                y= False;
            else:
                del userPairs[x]
                break
        if y == session["user"]:
            emit("disconnect", x, room = x)
            gameBoards[x] = game()
            userPairs[x] = False
            break
    print(userPairs)
    print(gameBoards)


@socketio.on('victory')
def victory(msg):
    #get opponent
    opponent = ""
    for x, y in userPairs.items():
        if x == session["user"]:
            opponent = y
            break
        if y == session["user"]:
            opponent = x
            break
    emit("victory", msg, room = opponent)
    emit("victory", msg, room = session["user"])

@socketio.on('message')
def handleMessage(msg):
    #get opponent
    opponent = ""
    for x, y in userPairs.items():
        if x == session["user"]:
            opponent = y
            break
        if y == session["user"]:
            opponent = x
            break
    # message sends which player made a move and to which cell
    player = msg.split()[0]
    cell = msg.split()[1]
    boardNum = msg.split()[2]
    win = 'f'
    #if player wins or draw
    move = game.move(gameBoards[session["user"]], player, int(cell),int(boardNum))

    if(move=="win 10"):
        win = 't 10'
        game.reset(gameBoards[session["user"]])
    elif(move.split()[0]=="win"):
        win = 't '+move.split()[1]
    elif(move=="draw 10"):
        win = 'd'
        game.reset(gameBoards[session["user"]])
    if(not move=="bad 10"):
        #send player, move, and if they have won
        send(player+" "+cell+" "+boardNum+" "+win, room = opponent)
        send(player+" "+cell+" "+boardNum+" "+win, room = session["user"])

@app.route("/", methods = ["POST","GET"])
def home():
    session.clear()
#place username in session
    if request.method == "POST" :
        if (request.form["name"] not in userPairs) and (request.form["name"] not in userPairs.values()):
            session["user"] = request.form["name"].replace(" ", "-")

# get list of users looking for a game, connect to random one
            openGames = []
            for x, y in userPairs.items():
                if not y:
                    openGames.append(x)

#if there are no games, create one
            if not openGames:
                userPairs[session["user"]] = False;
                gameBoards[session["user"]] = game()

            else:
                opp = random.choice(openGames)
                userPairs[opp]= session["user"]
                gameBoards[session["user"]] = gameBoards[opp]

            return redirect(url_for("play"))
#if name is taken, stay on this page and try again
        else:
            return render_template("home.html",taken = "That name is currently taken")
    return render_template("home.html")

@app.route("/game")
def play():

# if the username hasnt been set, return home
#if player quits a game, return home

    if not session.get("user"):
        return redirect(url_for("home"))
    if session.get("inGame"):
        return redirect(url_for("home"))
    try:
        user = session["user"]
        session["inGame"] = True
        return render_template("game.html", user=user)
    except:
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run()

def getOpponent():
    for x, y in userPairs.items():
        if x == session["user"]:
            return y
        if y == session["user"]:
            return x
