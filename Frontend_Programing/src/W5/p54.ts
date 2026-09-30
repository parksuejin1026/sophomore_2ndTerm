// 튜플에 forEach
const student: [string, number] = ["홍길동", 20];
student.forEach((value) => {
console.log(value);
})

// 튜플에 map
const numbers: [number, number, number] = [10, 20, 30];
const result = numbers.map(num => num * 2);
console.log(result);

// 연습해보기
const products : [string, string, string] = ["샴푸", "폼클랜징", "바디워시"];
products.forEach((e) => {
    console.log(e);
})
const lengthPlus = products.map(p => `${p}는 ${p.length}개 챙겨`);
console.log(lengthPlus);