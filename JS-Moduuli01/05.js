"use strict";

const year = parseInt(prompt("Enter the year"));
let result = document.querySelector('#result');

if ((year % 4 == 0 && year % 100 != 0) || year % 400 == 0) {
  result.innerHTML = `Year ${year} is a leap year.`;
} else {
  result.innerHTML = `Year ${year} is not a leap year.`;
}
