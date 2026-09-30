const user: {
name: string;
age: number;
} = {
name: "홍길동",
age: 20
};
// 기존 방식
const userName = user.name;
const userAge = user.age;
console.log(userName); // 홍길동
console.log(userAge); // 20
// 객체 구조 분해 할당
const { name: nName, age: nAge } = user;
console.log(nName); // 홍길동
console.log(nAge); // 20
const fruits = ["사과", "오렌지", "딸기"]; // 배열
const data: { // 객체
0: string;
1: string;
2: string;
length: number;
} = {
0: "사과",
1: "오렌지",
2: "딸기",
length: 3,
};
console.log(data[0]); // 사과
console.log(data.length); // 3
console.log(Array.isArray(fruits)); // true
console.log(Array.isArray(data)); // false