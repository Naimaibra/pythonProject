function checkPrime() {
  const inputNumber = document.getElementById('inputNumber').value;
  const resultElement = document.getElementById('result');

  resultElement.textContent = '';


  if (!Number.isInteger(+inputNumber) || +inputNumber < 2) {
    alert('Please enter a valid integer greater than or equal to 2.');
    return;
  }

  if (isPrime(+inputNumber)) {
    resultElement.textContent = `${inputNumber} is a prime number.`;
  } else {
    resultElement.textContent = `${inputNumber} is not a prime number.`;
  }
}

function isPrime(number) {
  if (number < 2) {
    return false;
  }

  for (let i = 2; i <= Math.sqrt(number); i++) {
    if (number % i === 0) {
      return false;
    }
  }

  return true;
}
