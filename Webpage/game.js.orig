// Lobby player options
const blackjackSelect = document.querySelector('#blackjack-select');
const pokerSelect = document.querySelector('#poker-select');
const cardShuffle = document.querySelector('#card-shuffle');
const readySelect = document.querySelector('#ready-select');
const lobbyGamestate = document.querySelector('#lobby-gamestate');
// Blackjack elements
const dealerHand = document.querySelector("#dealer-hand");
const dealerScore = document.querySelector("#dealer-score");
const blackjackHand = document.querySelector("#blackjack-hand");
const blackjackScore = document.querySelector("#blackjack-score");
const blackjackChips = document.querySelector("#blackjack-chips");
const blackjackGamestate = document.querySelector("#blackjack-gamestate");
// Blackjack player options
const blackjackInput = document.querySelector("#blackjack-input");
const blackjackBet = document.querySelector("#blackjack-bet");
const hit = document.querySelector("#hit");
const stand = document.querySelector("#stand");
const double = document.querySelector("#double");
// Poker elements
const pokerComm1 = document.querySelector('#comm1');
const pokerComm2 = document.querySelector('#comm2');
const pokerComm3 = document.querySelector('#comm3');
const pokerTurn = document.querySelector('#turn');
const pokerRiver = document.querySelector('#river');
const poker1 = document.querySelector('#poker1');
const poker2 = document.querySelector('#poker2');
const pokerGamestate = document.querySelector("#poker-gamestate");
// Poker player options
const pokerInput = document.querySelector("#poker-input");
const betBtn = document.querySelector('#bet');
const checkBtn = document.querySelector('#check');
const callBtn = document.querySelector('#call');
const raiseBtn = document.querySelector('#raise');
const foldBtn = document.querySelector('#fold');
// Sections for each game page
const lobby = document.querySelector('#lobby');
const blackjack = document.querySelector('#Blackjack');
const poker = document.querySelector('#Texas Holdem');


const elements = [
  { id: "lobby-gamestate", variable: lobbyGamestate },  
  { id: "dealer-hand", variable: dealerHand },
  { id: "dealer-score", variable: dealerScore },
  { id: "blackjack-hand", variable: blackjackHand },
  { id: "blackjack-score", variable: blackjackScore },
  { id: "blackjack-chips", variable: blackjackChips },
  { id: "blackjack-gamestate", variable: blackjackGamestate },
  { id: "comm1", variable: pokerComm1 },
  { id: "comm2", variable: pokerComm2 },
  { id: "comm3", variable: pokerComm3 },
  { id: "turn", variable: pokerTurn },
  { id: "river", variable: pokerRiver },
  { id: "poker1", variable: poker1 },
  { id: "poker2", variable: poker2 },
  { id: "poker-gamestate", variable: pokerGamestate }
];

const pages = [
  { id: "lobby", variable: lobby },
  { id: "Blackjack", variable: blackjack }
  //{ id: "Texas Holdem", variable: poker }
];

// Connection to server and page toggles
const username = document.getElementById("username").value;
const socket = new WebSocket("ws://localhost:1337/");
var gamemode = "lobby"

socket.onmessage = (event) => {
  var data = JSON.parse(event.data);
  console.log(data)
  
  // Update each element in the html file to their new gamestate if applicable 
  for (const element of elements) {
    const value = data[element.id];
    if (value !== undefined) {
      if("gamestate" in data){
          writeRows(data);
      }
      else if (["dealer-hand", "blackjack-hand", "community", "poker-hand"].includes(element.id)){
        writeCards(element.id, data);
      }
      else{
        element.variable.innerHTML = value;
      }
    }
  }

  // Loop through all gamemode pages and show/hide them based on the current gamemode
  pages.forEach((page) => {
    if (page.id == data.gamemode) {
      page.variable.style.display = "block";
    } else {
      page.variable.style.display = "none";
    }
  });
};

// When a client load the page, they are either in the lobby 
// or are put back into the game if they're reconnecting 
socket.onopen = (event) =>{send("connection");}

// Lobby event listeners
blackjackSelect.addEventListener("click", function() {send("setgame", "Blackjack");});

pokerSelect.addEventListener("click", function() {send("setgame", "Texas Holdem");});

cardShuffle.addEventListener("click", function() {send("shuffle");});

readySelect.addEventListener("click", function() {send("Ready");});


// Blackjack event listeners

blackjackBet.addEventListener("click", function() {send("bet", blackjackInput.value);});

hit.addEventListener("click", function() {send("hit");});

stand.addEventListener("click", function() {send("stand");});

double.addEventListener("click", function() {send("double");});

// Poker event listeners









function writeCards(id, data){
  var hand = data[id];
  var cards = "";

  hand.forEach((card => {
    cards += `<div class="card"><img src="http://localhost/Htmls/PNG-cards-1.3/` + card + `.png"></div>"`
  }));

  elements[id].innerHTML = cards;
}

function writeRows(data){
  // Variable for creating table rows might be changed based on current gamemode value
  var rows = "<tr><th>Player</th><th>Bet</th><th>Status</th></tr>"
  var table = lobbyGamestate;
  switch (data["gamemode"])
  {
    case "lobby":
      rows = "<tr><th>Player</th><th>Game Mode</th><th>Status</th></tr>"
      break;
    case "Blackjack":
      table = blackjackGamestate;
      break;
    case "Texas Holdem":
      table = pokerGamestate;
      break;
  }

  // Variable for green/"winning" table elements, switch to red if player reached unplayable state
  var winning = "win"
  if(["Busted!", "Folded!", "waiting", "Lost!"].includes(player[1])){winning = "loss"}

  value.forEach((player => {
    // Highlight will invert the colors for the client's position in the table
    var highlight = "";
    if(player[1] == username){
      const highlight = `class="highlighted"`; 
    }
    // Fill in gamestate table line by line
    if(data["gamemode"] == "lobby"){
      rows += "<tr" + highlight + "><td>" + player[0] + "</td><td>" + player[3] + "</td><td class='" + winning + "'>" + player[1]+ "</td></tr>";
    }else{
      rows += "<tr" + highlight + "><td>" + player[0] + "</td><td>" + player[2] + "</td><td class='" + winning + "'>" + player[1]+ "</td></tr>";
    }
  })); 

  // Update the table
  table.innerHTML = rows;
}

function send(action, additional = null) {
  const update = {
    action: action,
    username: username
  };

  if(additional != null){
    update.additional = additional;
  }

  socket.send(JSON.stringify(update));
}