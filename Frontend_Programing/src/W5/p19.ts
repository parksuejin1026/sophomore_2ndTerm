// 함수 선언문
function add(a: number, b: number): number {
return a + b;
}
console.log(add(10, 20)); // 30
// 함수 표현식
const add2 = function (a: number, b: number): number {
return a + b;
};
console.log(add2(10, 20)); // 30
// 화살표 함수
const add3 = (a: number, b: number): number => {
return a + b;
};
console.log(add3(10, 20)); // 30