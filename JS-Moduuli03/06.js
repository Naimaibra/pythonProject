
document.addEventListener("DOMContentLoaded", function() {

  // Use const for variables that won't be reassigned
  const buttonElement = document.getElementById("myButton");

  // Add a click event listener to the button
  buttonElement.addEventListener("click", function() {
    // Display an alert when the button is clicked
    alert("Button Clicked");
  });
});
