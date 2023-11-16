"use strict";
function findLeapYears() {
  const startYearInput = document.getElementById('startYear');
  const endYearInput = document.getElementById('endYear');
  const leapYearsList = document.getElementById('leapYearsList');


  leapYearsList.innerHTML = '';

  const startYear = parseInt(startYearInput.value);
  const endYear = parseInt(endYearInput.value);

  if (isNaN(startYear) || isNaN(endYear) || startYear > endYear) {
    alert('Invalid input. Please enter valid years.');
    return;
  }

  for (let year = startYear; year <= endYear; year++) {
    if (isLeapYear(year)) {
      const listItem = document.createElement('li');
      listItem.textContent = year;
      leapYearsList.appendChild(listItem);
    }
  }
}

function isLeapYear(year) {
  // Leap year logic
  return (year % 4 === 0 && year % 100 !== 0) || (year % 400 === 0);
}
