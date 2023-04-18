// Lobby player options
const blackjackSelect = document.querySelector('#blackjack-select');
const pokerSelect = document.querySelector('#poker-select');
const cardShuffle = document.querySelector('#card-shuffle');
const readySelect = document.querySelector('#ready-select');
// Blackjack elements
const dealerHand = document.querySelector("#dealer-hand");
const dealerScore = document.querySelector("#dealer-score");
const blackjackHand = document.querySelector("#blackjack-hand");
const playerScore = document.querySelector("#player-score");
const blackjackChips = document.querySelector("#blackjack-chips");
const blackjackGameState = document.querySelector("#blackjack-gamestate");
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
// Poker player options
const betBtn = document.querySelector('#bet');
const checkBtn = document.querySelector('#check');
const callBtn = document.querySelector('#call');
const raiseBtn = document.querySelector('#raise');
const foldBtn = document.querySelector('#fold');
// Sections for each game page
const lobby = document.querySelector('#lobby');
const blackjack = document.querySelector('#blackjack');
const poker = document.querySelector('#poker');
// Connection to server
const username = document.getElementById("username").value;
const socket = new WebSocket("ws://localhost:1337/");

socket.onmessage = (event) => {
  alert(event.data);
};

socket.onopen = (event) =>{
  lobby.style.display = "none";
  blackjack.style.display = "block";
  poker.style.display = "none";

}

// Add event listeners
blackjackInput.addEventListener("keypress", function (event) {
  if (event.key === "Enter") {
    // handle input
  }
});

blackjackBet.addEventListener("click", function () {
  alert("Clicked!");
  socket.send(blackjackInput.value);
});

hit.addEventListener("click", function () {
  // handle hit
});

stand.addEventListener("click", function () {
  // handle stand
});

double.addEventListener("click", function () {
  // handle double
});



// Event handlers

function handleReadyClick() {
  // Check if all players are ready
  let allReady = true;
  playerRows.forEach((row, index) => {
    if (index !== 0) { // Skip table header row
      const statusCell = row.querySelector('td:last-child');
      if (!statusCell.classList.contains('ready')) {
        allReady = false;
      }
    }
  });
  
  if (allReady) {
    alert('Game starting!');
    // Reset player statuses
    playerRows.forEach((row, index) => {
      if (index !== 0) {
        const statusCell = row.querySelector('td:last-child');
        statusCell.classList.remove('ready', 'not-ready');
        statusCell.classList.add('not-ready');
      }
    });
  } else {
    alert('Not all players are ready yet.');
  }
}
