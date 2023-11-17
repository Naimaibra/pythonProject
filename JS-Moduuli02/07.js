// script.js
"use strict";

function getRandomDiceRoll(sides) {
  return Math.floor(Math.random() * sides) + 1;
}

function main() {
  let sides = prompt("Enter the number of sides on the dice:");

  if (isNaN(sides) || sides <= 0) {
    alert("Please enter a valid number of sides.");
    return;
  }

  sides = parseInt(sides);
  let resultList = document.getElementById('resultList');
  let rollResult;

  while ((rollResult = getRandomDiceRoll(sides)) !== sides) {
    let listItem = document.createElement('li');
    listItem.textContent = `Dice Roll: ${rollResult}`;
    resultList.appendChild(listItem);
  }
}

main();
