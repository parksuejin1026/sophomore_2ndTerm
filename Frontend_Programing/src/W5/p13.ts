let number: number = 1;
let sum: number = 0;
while (sum < 100) {
sum += number;
console.log(`${number}을 더함 → 합계: ${sum}`);
number++;
}
console.log(`반복 종료`);
console.log(`마지막 숫자: ${number - 1}`);
console.log(`최종 합계: ${sum}`);