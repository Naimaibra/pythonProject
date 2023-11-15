
"use strict";
// fetch HTML element

const fillName = document.querySelector('.fillName');
const name = prompt('Please give your name:');
console.log(name);

fillName.innerHTML = `Hello, ${name}, What's good!`;

