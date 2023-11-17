  "use strict";


// script.js
let numbers = [];

while (true) {
  let userInput = prompt("Enter a number (enter 0 to stop):");
  let number = parseFloat(userInput);

  if (isNaN(number)) {
    alert("Please enter a valid number.");
    continue;
  }

  if (number === 0) {
    break;
  }

  numbers.push(number);
}

numbers.sort((a, b) => b - a);

console.log("Numbers in descending order:", numbers);
