// setTimeout()
console.log('1. 프로그램 시작');
setTimeout(() => {
    console.log("2.2초 후 실행");
}, 2000);
console.log("3. 프로그램 종료");
// setInterval(), clearInterval()
let count = 1;
const timerId = setInterval(() => {
    console.log(`${count}초 경과`);
    count++;
    if (count > 5) {
        clearInterval(timerId);
        console.log("타이머 종료");
    }
}, 1000);
export {};
