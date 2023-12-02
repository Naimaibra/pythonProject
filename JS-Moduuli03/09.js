document.addEventListener("DOMContentLoaded", function() {
  // DOM is ready, now you can manipulate the elements

  // Use const for variables that won't be reassigned
  const calculateButton = document.getElementById("calculate");
  const resultElement = document.getElementById("result");

  // Add click event listener to the calculate button
  calculateButton.addEventListener("click", function() {
    // Get the calculation string from the input field
    const calculationString = document.getElementById("calculation").value;

    // Check if the calculation string is not empty
    if (calculationString.trim() === "") {
      resultElement.textContent = "Please enter a valid calculation.";
    } else {
      // Split the calculation string into operands and operator
      const operators = ["+", "-", "*", "/"];
      let operator = "";

      for (const op of operators) {
        if (calculationString.includes(op)) {
          operator = op;
          break;
        }
      }

      if (operator === "") {
        resultElement.textContent = "Invalid operation in the calculation.";
      } else {
        const operands = calculationString.split(operator);

        // Convert operands to integers
        const operand1 = parseInt(operands[0].trim(), 10);
        const operand2 = parseInt(operands[1].trim(), 10);

        // Perform the operation and display the result
        switch (operator) {
          case "+":
            resultElement.textContent = `Result: ${operand1 + operand2}`;
            break;
          case "-":
            resultElement.textContent = `Result: ${operand1 - operand2}`;
            break;
          case "*":
            resultElement.textContent = `Result: ${operand1 * operand2}`;
            break;
          case "/":
            // Check for division by zero
            resultElement.textContent = operand2 !== 0
              ? `Result: ${Math.floor(operand1 / operand2)}`
              : "Cannot divide by zero.";
            break;
          default:
            resultElement.textContent = "Invalid operation in the calculation.";
        }
      }
    }
  });
});
