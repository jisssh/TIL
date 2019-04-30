function sleep_3s() {
    setTimeout(() => {console.log('wake up!')}, 3000)
}




const logEnd = () => {
    console.log('END')
};
console.log('startsleeping');
sleep_3s();
console.log('end');