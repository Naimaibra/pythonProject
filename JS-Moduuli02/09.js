// script.js
"use strict";

function even(numbersArray) {
  return numbersArray.filter(number => number % 2 === 0);
}

document.addEventListener("DOMContentLoaded", function() {
  // Example array
  let originalArray = [2, 7, 4];

  // Print the original array to the HTML document
  document.getElementById('originalArray').textContent = `Original Array: [${originalArray.join(', ')}]`;

  // Call the even function and print the new array to the HTML document
  let newArray = even(originalArray);
  document.getElementById('newArray').textContent = `New Array with Even Numbers: [${newArray.join(', ')}]`;
});
