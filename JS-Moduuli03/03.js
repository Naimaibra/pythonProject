"use strict"; // Enable strict mode

document.addEventListener("DOMContentLoaded", function() {
  // DOM is ready, now you can manipulate the elements


  const targetElement = document.querySelector("#target");

  // Array of names
  const names = ['John', 'Paul', 'Jones'];

  for (let i = 0; i < names.length; i++) {

    const listItem = document.createElement("li");

    listItem.textContent = names[i];

    targetElement.appendChild(listItem);
  }
});
