function multiply2(a, b = 1) {
    return a * b;
}
console.log(multiply2(10));
console.log(multiply2(10, 5));
// ...numbers는 여러 개의 인수를 하나의 배열로 받아옴
function sumAll(...numbers) {
    return numbers.reduce((acc, num) => acc + num, 0);
}
console.log(sumAll(1, 2, 3));
export {};
