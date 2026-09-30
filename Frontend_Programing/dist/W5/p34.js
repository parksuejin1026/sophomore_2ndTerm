const fruits = ["사과", "오렌지", "배", "딸기"];
console.log(fruits.length); // 4
console.log(fruits[0]); // 사과
console.log(fruits[2]); // 배
console.log(fruits.at(0)); // 사과
console.log(fruits.at(-1)); // 딸기
const fruits2 = ["사과", "오렌지", "배"];
// 특정 인덱스에 값 추가
fruits2[3] = "딸기";
// 맨 앞에 추가
fruits2.unshift("수박");
// 맨 뒤에 추가
fruits2.push("포도");
console.log(fruits2);
export {};
