const fruits = ["사과", "오렌지", "배", "딸기", "수박"];
// 1. 배열 자르기
const selected = fruits.slice(1, 4);
console.log(selected);
// ["오렌지", "배", "딸기"] => 1, 2, 3
console.log(fruits);
// ["사과", "오렌지", "배", "딸기", "수박"]
// 2. 배열 합치기
const tropical = ["망고", "바나나"];
const allFruits = fruits.concat(tropical);
console.log(allFruits);
// ["사과", "오렌지", "배", "딸기", "수박", "망고", "바나나"]