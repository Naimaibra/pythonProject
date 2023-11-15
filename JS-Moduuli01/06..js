"use strict";
// Confirmation window
const answer = confirm("Should I calculate the square root?");
console.log(answer);

if (answer) {
  const number = parseInt(prompt("Please give me a number:"));
  const result = document.querySelector('#result');
  if (number >= 0) {
    let squareRoot = Math.sqrt(number);
    result.innerHTML = `The square root of ${number} is ${squareRoot}`;
  } else {
    result.innerHTML = "The square root of a negative number is not defined.";
  }
} else {
  document.querySelector('#result').innerHTML = "The square root is not calculated.";
}
