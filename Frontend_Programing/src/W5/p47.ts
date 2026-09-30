const numbers: number[] = [1, 2, 3, 4];
const result = numbers.map( (num) => {
    return num * 2;
});
console.log(result);
// map 줄여서 표현
const result_short = numbers.map((num) => num * 2);
console.log(result_short);
// Return 이 없으면 result2 는 빈값이 들어감
const result2 = numbers.map( (num) => {
    num * 2;
});
console.log(result2);

// map 연습
const result3 = numbers.map((e, i) => {
    return `${e}의 세 제곱은 ${e ** 3} ${i}번쨰 인덱스`;
})
console.log(result3)