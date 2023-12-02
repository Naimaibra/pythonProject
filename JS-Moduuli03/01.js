for (const useStrictElement of 'use strict!') {

}

document.addEventListener("DOMContentLoaded", function() {
  //now you can manipulate the elements

  const targetElement = document.querySelector("#target");

  // Add HTML content using innerHTML property
  targetElement.innerHTML = `
    <li>First item</li>
    <li>Second item</li>
    <li>Third item</li>
  `;

  // Add class "my-list" to the element
  tarSgetElement.classList.add("my-list");
});
