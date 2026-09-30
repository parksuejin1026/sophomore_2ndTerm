for (let i = 0; i < 100; i++) {
    const number = i + 1;
    // 50이 되면 반복 종료
    if (number === 50) {
        break;
    }
    // 3의 배수는 건너뛰기
    if (number % 3 === 0) {
        continue;
    }
    console.log(number);
}
export {};
