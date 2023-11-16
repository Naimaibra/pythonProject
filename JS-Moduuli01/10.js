function calculateProbability() {
  const numberOfDice = parseInt(document.getElementById('numberOfDice').value);
  const desiredSum = parseInt(document.getElementById('desiredSum').value);
  const probabilityResultElement = document.getElementById('probabilityResult');

  // Clear previous results
  probabilityResultElement.textContent = '';

  // Check if inputs are valid
  if (isNaN(numberOfDice) || isNaN(desiredSum) || numberOfDice < 1 || desiredSum < numberOfDice || desiredSum > numberOfDice * 6) {
    alert('Please enter valid inputs.');
    return;
  }

  const totalPossibleOutcomes = Math.pow(6, numberOfDice);
  const favorableOutcomes = countFavorableOutcomes(numberOfDice, desiredSum);

  const probability = favorableOutcomes / totalPossibleOutcomes;

  probabilityResultElement.textContent = `Probability: ${probability.toFixed(4)}`;
}

function countFavorableOutcomes(numberOfDice, desiredSum, currentSum = 0, currentDice = 0) {
  if (currentDice === numberOfDice) {
    return currentSum === desiredSum ? 1 : 0;
  }

  let count = 0;
  for (let i = 1; i <= 6; i++) {
    count += countFavorableOutcomes(numberOfDice, desiredSum, currentSum + i, currentDice + 1);
  }

  return count;
}

