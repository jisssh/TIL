function sleep_3s() {
    console.log('INVOKE');
    setTimeout(() => {console.log('WAKE UP!')}, 3000)
}

const logEnd = () => {
    console.log('END')
};
console.log('start sleeping');
sleep_3s();
console.log('end');