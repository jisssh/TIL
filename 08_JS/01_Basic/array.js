const numbers = [1, 2, 3, 4];

numbers[0]; // 1
numbers[-1]; // undefined
numbers.length; // 4

/*
원본이 달라지는 methods
 */
numbers.reverse(); // [4, 3, 2, 1]
numbers; // [4, 3, 2, 1]
numbers.reverse(); // [1, 2, 3, 4]

numbers.push('a'); // return 5 (new length)
numbers; // [1, 2, 3, 4, "a"]

numbers.pop(); // return "a" (pop 한 결과)
numbers; // [1, 2, 3, 4]

numbers.unshift("a"); // return 5 (new length)
numbers; // ["a", 1, 2, 3, 4]

numbers.shift(); // return "a"
numbers; // [1, 2, 3, 4]

/*
복사본 return 하는 methods ( 결과는 바뀌지 않음 )
 */
numbers.includes(1); // return true
numbers.includes(0); // return false
numbers; // [1, 2, 3, 4]

numbers.push('a', 'a'); // 'test'
numbers.indexOf('a'); // 앞에있는 요소부터
numbers.indexOf('b'); // return -1 === 없다.

numbers.join('-'); // '1-2-3-4-a-a'
numbers.join(); // '1,2,3,4,a,a'
numbers.join(''); // '1234aa'


