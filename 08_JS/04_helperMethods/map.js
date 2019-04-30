//ES5 for loop
// var numbers = [1, 2, 3];
// var doubleNumbers = [];
//
// for (var i = 0; i < numbers.length; i ++) {
//     doubleNumbers.push(numbers[i] * 2);
// }
//
// console.log(doubleNumbers);


//ES6+
const numbers = [1, 2, 3];

function double(n) {
    return n * 2;
}

const doublenumbers = numbers.map(double);

const tripleNumbers = numbers.map(number => {
    return number * 3
});
console.log(tripleNumbers);

const images = [
    {height: 34, width: 39},
    {height: 34, width: 29},
];

const imageAreas = images.map(image => {
    return image.height * image.width;
});
console.log(imageAreas);


/*
    아래의 pluck 함수를 완성하시오.
    pluck 함수는 배열 (array) 과 요소 이름 (key) 의 문자열울



 */
function pluck(array, property) {
    const newArray = array.map( e => {
        if (e[property]) return e[property]
    });
    return newArray;
}
const paints = [
    {color: 'red'},
    {color: 'blue'},
    {color: 'white'},
    {smell:'aaaa'},
];

console.log(pluck(paints, 'color'));
console.log(pluck(paints, 'smell'));