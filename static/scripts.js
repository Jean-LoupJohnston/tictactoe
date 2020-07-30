var board;
const player1 = "X";
const player2 = "O";
var socket = io.connect('http://127.0.0.1:5000')
const cells = document.querySelectorAll(".cell");

//start game
start();
function start()
{
  socket.on('connect', function() {
		//socket.send('User joined');
	});

  //accept broadcast from sever and update board
  socket.on('message', function(msg) {
  		document.getElementById(msg.split(" ")[1]).innerHTML =  "<img src='static/a.webp' width = '90px' height = '90px'>";
      if(msg.split(" ")[2]=="t")
      {
        document.getElementById("win").innerText = "Player "+msg.split(" ")[0]+" won"
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
  document.getElementById(x.target.id).innerHTML =  "<img src='static/a.webp' width = '90px' height = '90px'>";
  socket.send(player1+" "+x.target.id)
}
