var board;

var currentPlayer ="";
var playerTurn = "X";

var socket = io.connect('http://127.0.0.1:5000')
const cells = document.querySelectorAll(".cell");

//start game
start();
function start()
{
//On connection, set current player
  socket.on('connect', function(msg) {
    currentPlayer = msg
	});

  //accept broadcast from server and update board
  socket.on('message', function(msg) {
    console.log(msg)
    if(msg.split(" ")[0]=="X")
    {
      document.getElementById(msg.split(" ")[1]).innerHTML =  "<img id="+msg.split(" ")[1]+" src='static/a.webp' width = '90px' height = '90px'>"
      playerTurn = "O"
    }
    else {
      {
          document.getElementById(msg.split(" ")[1]).innerHTML =  "<img id="+msg.split(" ")[1]+" src='static/c.png' width = '90px' height = '90px'>";
            playerTurn = "X"
      }
    }
    //if victory
      if(msg.split(" ")[2]=="t")
      {
        resetBoard(msg.split(" ")[0])
      }
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
    {socket.send(currentPlayer+" "+x.target.id)}
}

//after someone wins, reset board
function resetBoard(player)
{
  for(var i = 0; i<cells.length; i++)
  {
    cells[i].innerHTML =  ""
    playerTurn = "X"
    document.getElementById("win").innerText = "Player "+player+" won"
  }
}
