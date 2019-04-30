// This is Comment

// if (checkLongStr(concat('Happy', 'Hacking'))) {
//     console.log('LONG STRING');
// }
// else {
//     console.log('SHORT STRING');
// }

const concat = (str1, str2) => `${str1} - ${str2}`;
const checkLongStr = (string) => string.length > 10;
checkLongStr(concat('Happy', 'Hacking')) ?  console.log('LONG STRING'):console.log('SHORT STRING');

console.log(
    checkLongStr(concat('Happy', 'Hacking')) ? ('LONG STRING'):('SHORT STRING')
);