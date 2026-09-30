const fruits = ["사과", "바나나", "포도", "바나나", "딸기", "수박"];
console.log("처음:", fruits);
// 1. 요소 수정
fruits[2] = "오렌지";
console.log("수정:", fruits);
// 2. 마지막 요소 삭제
fruits.pop();
console.log("pop:", fruits);
// 3. 첫 번째 요소 삭제
fruits.shift();
console.log("shift:", fruits);
// 4. 중간 요소 삭제
fruits.splice(1, 1);
console.log("splice:", fruits);
// 5. 요소 찾기
console.log(fruits.includes("바나나")); // true
console.log(fruits.indexOf("바나나")); // 0
console.log(fruits.lastIndexOf("바나나")); // 1
export {};
