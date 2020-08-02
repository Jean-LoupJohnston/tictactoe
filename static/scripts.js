var board;

var currentPlayer ="";


const img1 = "<img src='static/a.webp' width = '90px' height = '90px'>";
const img2 = "<img src='static/c.png' width = '90px' height = '90px'>";
var socket = io.connect('http://127.0.0.1:5000')
const cells = document.querySelectorAll(".cell");

//start game
start();
function start()
{
//On connection, set current player
  socket.on('connect', function(msg) {
    currentPlayer = msg
    console.log(msg)
	});



  //accept broadcast from sever and update board
  socket.on('message', function(msg) {
    if(msg.split(" ")[0]=="X")
    {
      document.getElementById(msg.split(" ")[1]).innerHTML =  img1;
    }
    else {
      {
              document.getElementById(msg.split(" ")[1]).innerHTML =  img2;
      }
    }
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

//when clicking a cell
function click(x)
{
  socket.send(currentPlayer+" "+x.target.id)
}

//after someone wins, reset board
function resetBoard(player)
{
  for(var i = 0; i<cells.length; i++)
  {
    cells[i].innerHTML =  ""
    document.getElementById("win").innerText = "Player "+player+" won"
  }
}
