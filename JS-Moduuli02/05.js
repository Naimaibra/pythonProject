  "use strict";
// script.js

let numbers = new Set(); // Using a Set to store unique numbers

while (true) {
  let userInput = prompt("Enter a number (enter 'stop' to finish):");

  if (userInput.toLowerCase() === 'stop') {
    break;
  }

  let number = parseFloat(userInput);

  if (isNaN(number)) {
    alert("Please enter a valid number.");
    continue;
  }

  if (numbers.has(number)) {
    alert("This number has already been entered. Stopping the program.");
    break;
  }

  numbers.add(number);
}

let sortedNumbers = Array.from(numbers).sort((a, b) => a - b);

console.log("Numbers in ascending order:", sortedNumbers);
