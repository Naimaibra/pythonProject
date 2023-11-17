"use strict";

// script.js

function getRandomDiceRoll() {
  return Math.floor(Math.random() * 6) + 1;
}

function main() {
  let resultList = document.getElementById('resultList');
  let rollResult;

  while ((rollResult = getRandomDiceRoll()) !== 6) {
    let listItem = document.createElement('li');
    listItem.textContent = `Dice Roll: ${rollResult}`;
    resultList.appendChild(listItem);
  }
}

main();
