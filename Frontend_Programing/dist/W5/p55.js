// 튜플에 includes, indexOf 사용
const fruits = ["사과", "오렌지", "딸기"];
console.log(fruits.includes("사과"));
console.log(fruits.indexOf("딸기"));
// 튜플에 슬라이싱
const student = ["홍길동", 20, "서울"];
const result = student.slice(0, 2); // 0~1번째 인덱스
console.log(result);
// 연습해보기
const games = ["League of Legends", "Maple Story", "Lost Ark"];
console.log(games.includes("MineCraft"));
console.log(games.indexOf("Lost Ark"));
console.log(games.slice(0, 2));
export {};
