

document.addEventListener("DOMContentLoaded", function() {
  // DOM is ready, now you can manipulate the elements

  // Use const or let to declare variables
  const targetElement = document.querySelector("#target");

  // Create list items
  const listItem1 = document.createElement("li");
  listItem1.textContent = "First item";

  const listItem2 = document.createElement("li");
  listItem2.textContent = "Second item";
  listItem2.classList.add("my-item"); // Add class "my-item" to the second list item

  const listItem3 = document.createElement("li");
  listItem3.textContent = "Third item";

  // Append list items to the target element
  targetElement.appendChild(listItem1);
  targetElement.appendChild(listItem2);
  targetElement.appendChild(listItem3);
});
