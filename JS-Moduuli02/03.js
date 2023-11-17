"use strict";
// script.js

function getDogNames() {
  let dogNames = [];

  // Prompt the user for the names of six dogs
  for (let i = 1; i <= 6; i++) {
    let name = prompt(`Enter the name of dog ${i}:`);
    dogNames.push(name);
  }

  dogNames.sort(function(a, b) {
    return b.localeCompare(a);
  });

  // Display the names on the web page
  document.write("<h2>Dog Names (Reverse Alphabetical Order):</h2>");
  document.write("<ul>");
  for (let i = 0; i < dogNames.length; i++) {
    document.write(`<li>${dogNames[i]}</li>`);
  }
  document.write("</ul>");
}

// declaring the function
getDogNames();
