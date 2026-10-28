// clearTimeout()
const timeoutId: ReturnType<typeof setTimeout> = setTimeout(() : void =>
{
    console.log('3초 후 실행됩니다');
}, 3000);

console.log("timeoutId : " + timeoutId);
clearTimeout(timeoutId);

console.log('setTimeout 실행이 취소되었습니다.');

// clearInterval
let count : number = 1;

const intervalId: ReturnType <typeof setInterval> = setInterval((): void =>
{
    console.log(`${count}초 경과`);
    count++;

    if (count > 3) {
        console.log('intervalId : ' + intervalId);
        clearInterval(intervalId);
        console.log("반복 실행을 중지합니다.");
    }
}, 1000);