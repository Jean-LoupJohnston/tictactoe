var board;
const player1 = "X";
const player2 = "O";

const cells = document.querySelectorAll(".cell");
start();

function start()
{
  
  for(var i = 0; i<cells.length; i++)
  {
    cells[i].addEventListener('click',click,false);
  }
}
function click(x)
{
  document.getElementById(x.target.id).innerHTML =  "<img src='static/a.webp' width = '90px' height = '90px'>";
}
