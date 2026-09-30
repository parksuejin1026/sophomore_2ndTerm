const fruits = ["사과", "오렌지", "배", "딸기"];
// 1. 배열 → 문자열
const text1 = fruits.join();
const text2 = fruits.join(" / ");
console.log(text1);
// 사과,오렌지,배,딸기
console.log(text2);
// 사과 / 오렌지 / 배 / 딸기
// 2. 문자열 → 배열
const fruits2 = text2.split(" / ");
console.log(fruits2);
// ["사과", "오렌지", "배", "딸기"]
