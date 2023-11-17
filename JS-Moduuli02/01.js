"use strict";

let numbers = [];

// THis is using Prompt user for five numbers
for (let i = 0; i < 5; i++) {
  let userInput = prompt(`Enter number ${i + 1}:`);
  let number = parseFloat(userInput); // Convert user input to a number
  numbers.push(number);
}

// Print the numbers in reverse order
console.log("Numbers in reverse order:");

for (let i = numbers.length - 1; i >= 0; i--) {
  console.log(numbers[i]);
}
