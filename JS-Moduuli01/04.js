function sortStudent() {

    let studentName = document.querySelector('#studentName').value;


    let randomValue = Math.floor(Math.random() * 4) + 1;

    let house;
    switch (randomValue) {
        case 1:
            house = "Gryffindor";
            break;
        case 2:
            house = "Slytherin";
            break;
        case 3:
            house = "Hufflepuff";
            break;
        case 4:
            house = "Ravenclaw";
            break;
        default:
            house = "Unknown House";
    }


    let resultElement = document.querySelector('#result');
    resultElement.innerHTML = `${studentName}, you are in ${house}.`;
}
