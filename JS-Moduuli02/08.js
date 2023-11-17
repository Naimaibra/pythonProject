// script.js
"use strict";

function concat(stringsArray) {
  let result = '';

  for (let i = 0; i < stringsArray.length; i++) {
    result += stringsArray[i];
  }

  return result;
}

// Example array
let namesArray = ["Johnny", "DeeDee", "Joey", "Marky"];

// Call the concat function and print the result to the HTML document
document.getElementById('resultParagraph').textContent = concat(namesArray);
