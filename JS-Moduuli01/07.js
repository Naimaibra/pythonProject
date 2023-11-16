function rollDice(numberOfRolls) {
  let sum = 0;

  for (let i = 0; i < numberOfRolls; i++) {
    let diceResult = Math.floor(Math.random() * 6) + 1;
    console.log(`Roll ${i + 1}: ${diceResult}`);
    sum += diceResult;
  }

  console.log(`Sum of the rolls: ${sum}`);

}

const numberOfRolls = prompt("Enter the number of dice rolls:");

if (numberOfRolls !== null && !isNaN(numberOfRolls) && numberOfRolls > 0) {
  rollDice(Number(numberOfRolls));
} else {
  console.log("Invalid input. Please enter a positive number.");
}
