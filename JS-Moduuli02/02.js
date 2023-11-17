  "use strict";

// script.js

function getParticipantNames() {

  let participantCount = prompt("Enter the number of participants:");
  participantCount = parseInt(participantCount);

  if (isNaN(participantCount) || participantCount <= 0) {
    alert("Please enter a valid number of participants.");
    return;
  }

  let participantNames = [];

  for (let i = 1; i <= participantCount; i++) {
    let name = prompt(`Enter the name of participant ${i}:`);
    participantNames.push(name);
  }

  participantNames.sort();

  document.write("<h2>Participant Names:</h2>");
  document.write("<ol>");
  for (let i = 0; i < participantNames.length; i++) {
    document.write(`<li>${participantNames[i]}</li>`);
  }
  document.write("</ol>");
}

getParticipantNames();
