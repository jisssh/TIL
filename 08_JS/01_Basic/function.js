/*
        def my_function(arg1, arg2):
            ...
            return value

        func = lambda ar1, arg: value

 */
// 1. 함수 키워드 정의
function  add(num1, num2) {
    return num1 + num2;
}

// 2. 변수에 함수 로직 할당
// *****  함수는 const!!!!!!!!!!!!!!   *****
const sub = function(num1, num2) {
    return num1 - num2;
};
add(1,3);
sub(10, 4);

// 3. 함수 표현식 2가지
// 3-1
let mul = function (num1, num2) {
    return num1 * num2;
};
/*
    step 1: function 키워드를 없앤다.
    step 2: ( ) 와 [ ] 사이에 => 를 넣는다.
*/
mul = (num1, num2) => {
    return num1 * num2
};
/*
    step 1: 인자가 단 하나라면 ( ) 가 생략 가능하다.
    step2: 함수 블락안에 코드가 return 문 한 줄이라면, {} & return 키워드 삭제 가능하다.
 */
let square = function (num) {
    return num ** 2;
};
square = (num) => {
    return num ** 2;
};

square = num =>  num ** 2;
square = num => num ** 3;
square(3);

let noArgs = () => {
    return 'nothing'
};

noArgs = () => 'nothing';
oneArgs = a => 'one';
manArgs = (a, b, c, d, e) => 'many';

/*
Default Args
 */
function sayHello(name='jiss') {
    return `hi ${name}!`;
}
const sayHello = (name = 'jiss') => `hi ${name}!`;

sayHello(); // hi jiss!
sayHello('sanghyeon'); // hi sanghyeon!

// 익명 함수 실핼
(num => num ** 2)(4); // 16





