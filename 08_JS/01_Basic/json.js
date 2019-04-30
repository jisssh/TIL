const myObject = {
    coffee: 'Americano',
    icecream: 'Cookie and Cream',
};

const jsonData = JSON.stringify(myObject); // "{"coffee":"Americano","icecream":"Cookie and Cream"}"
console.log(typeof jsonData); // string

const parseData = JSON.parse(jsonData);
console.log(typeof parseData); // object
parseData.coffee; // "Americano"