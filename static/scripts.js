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
    currentPlayer = msg
	});

  //accept broadcast from server and update board
  socket.on('message', function(msg) {
    console.log(msg)
    id = (Number(msg.split(" ")[2])+1)+msg.split(" ")[1]
    console.log(id)

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
    //if victory
      if(msg.split(" ")[3]=="t")
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
    { socket.send(currentPlayer+" "+x.target.id%10 +" " +(Math.floor(x.target.id/10)-1))}
}

//after someone wins, reset board
function resetBoard(player)
{
  //if player won, send his name to server
  if(player == currentPlayer){
  socket.emit("victory", user)
}
//listen for winner name
socket.on('victory', function(msg) {
  document.getElementById("win").innerText = (msg+" wins!!")
});

  for(var i = 0; i<cells.length; i++)
  {
    cells[i].innerHTML =  ""
  }
  playerTurn = "X"
}
