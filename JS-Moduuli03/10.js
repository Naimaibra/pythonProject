
document.addEventListener("DOMContentLoaded", function() {


  const myForm = document.getElementById("myForm");
  const targetElement = document.getElementById("target");

  // Add submit event listener to the form
  myForm.addEventListener("submit", function(event) {
    // Prevent the default form submission
    event.preventDefault();


    const firstName = document.querySelector('[name="firstName"]').value;
    const lastName = document.querySelector('[name="lastName"]').value;

    // Display the result in the target element
    targetElement.textContent = `Your name is ${firstName} ${lastName}`;
  });
});
