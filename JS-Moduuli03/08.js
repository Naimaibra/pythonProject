document.addEventListener("DOMContentLoaded", function() {
  // DOcument is ready to manipulate the elements

  // Use const for variables that won't be reassigned
  const calculateButton = document.getElementById("calculate");
  const resultElement = document.getElementById("result");

  // Add click event listener to the calculate button
  calculateButton.addEventListener("click", function() {
    // Get the values from the input fields and dropdown
    const number1 = parseFloat(document.getElementById("number1").value);
    const number2 = parseFloat(document.getElementById("number2").value);
    const operation = document.getElementById("operation").value;

    // Perform the selected operation and display the result
    if (isNaN(number1) || isNaN(number2)) {
      resultElement.textContent = "Please enter valid numbers.";
    } else {
      switch (operation) {
        case "add":
          resultElement.textContent = `Result: ${number1 + number2}`;
          break;
        case "subtract":
          resultElement.textContent = `Result: ${number1 - number2}`;
          break;
        case "multiply":
          resultElement.textContent = `Result: ${number1 * number2}`;
          break;
        case "divide":
          // Check for division by zero
          resultElement.textContent = number2 !== 0
            ? `Result: ${number1 / number2}`
            : "Cannot divide by zero.";
          break;
        default:
          resultElement.textContent = "Invalid operation selected.";
      }
    }
  });
});
