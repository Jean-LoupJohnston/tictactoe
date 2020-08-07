var board;

var currentPlayer =""
var playerTurn = "X"
var socket = io.connect('http://127.0.0.1:5000')
const cells = document.querySelectorAll(".cell");

//start game
start();
function start()
{
//On connection, set current player
  socket.on('connect', function(msg) {
    if(msg){
      currentPlayer = msg.split(" ")[0]
        document.getElementById("waiting").innerHTML = "Playing against:"
        document.getElementById("waiting2").innerHTML = msg.split(" ")[1]
    }

	});

  //accept broadcast from server and update board
  socket.on('message', function(msg) {
    console.log(msg)
    id = (Number(msg.split(" ")[2])+1)+msg.split(" ")[1]

    if(msg.split(" ")[0]=="X")
    {
      document.getElementById(id).innerHTML =  "<img id="+id+" src='static/a.webp' width = '55px' height = '55px'>"
      playerTurn = "O"
    }
    else {
      {
          document.getElementById(id).innerHTML =  "<img id="+id+" src='static/c.png' width = '55px' height = '55px'>";
            playerTurn = "X"
      }
    }
//if bigboard victory
      if(msg.split(" ")[3]=="t" && msg.split(" ")[4]=="10")
      {
        resetBoard(msg.split(" ")[0], false)
      }
      else if(msg.split(" ")[3]=="t" )
      {

        if(msg.split(" ")[0]=="X")
        {document.getElementById(msg.split(" ")[4]+"a").innerHTML =  "<img  src='static/a.webp' width = '190px' height = '190px'>"
         document.getElementById(msg.split(" ")[4]+"b").style.visibility= "hidden"
        }
        else
        {document.getElementById(msg.split(" ")[4]+"a").innerHTML =  "<img  src='static/c.png' width = '190px' height = '190px'>"
         document.getElementById(msg.split(" ")[4]+"b").style.visibility = "hidden"
        }
      }

//if bigboard draw
      else if(msg.split(" ")[3]=="d")
      {
        resetBoard(msg.split(" ")[0], true)
      }
  	});

    socket.on('disconnect', function(msg) {
      resetBoard("Opponent left, "+msg+" wins!", false)
  	});



  for(var i = 0; i<cells.length; i++)
  {
    cells[i].addEventListener('click',click,false);
  }
}

//when clicking a cell, doesn't work if it's not player's turn
function click(x)
{

  if(currentPlayer==playerTurn)
    {socket.send(currentPlayer+" "+x.target.id%10 +" " +(Math.floor(x.target.id/10)-1))}
}

//after someone wins, reset board
function resetBoard(player, draw)
{
  if(draw)
  {
    document.getElementById("win").style.visibility = "visible"
    document.getElementById("win").innerText = ("Draw!")
  }
  //if player won, send his name to server
  else if(player == currentPlayer){
  socket.emit("victory", user)
}
//if opponent left
else{
  document.getElementById("win").style.visibility = "visible"
  document.getElementById("win").innerText = (player)
  document.getElementById("waiting").innerHTML = "Waiting for opponent..."
  document.getElementById("waiting2").innerHTML = ""
}
//listen for winner name
socket.on('victory', function(msg) {
  document.getElementById("win").style.visibility = "visible"
  document.getElementById("win").innerText = (msg+" wins!")
});

//reset boards
  for(var j = 0; j<9;j++)
  {
    document.getElementById(j+"a").innerHTML = ""
  }
  for(var j = 0; j<9;j++)
  {
    document.getElementById(j+"b").style.visibility = "visible"
  }
  for(var i = 0; i<cells.length; i++)
  {
    cells[i].innerHTML =  ""
  }
  playerTurn = "X"
}
