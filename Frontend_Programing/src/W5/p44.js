const scores = [[80, 90], [100, 80], [90, 70]];
// 1. 중첩 배열을 1차원 배열로 변환
const flatScores = scores.flat();
console.log(flatScores);
// [80, 90, 100, 80, 90, 70]
// 2. 배열을 특정 값으로 채우기
const result = new Array(5).fill(0);
console.log(result);
// [0, 0, 0, 0, 0]
// 3. Set으로 중복 제거
const uniqueScores = new Set(flatScores);
console.log(uniqueScores);
// Set {80, 90, 100, 70}
console.log(uniqueScores.size);
// 4
// 4. Set을 다시 배열로 변환
const finalScores = Array.from(uniqueScores);
console.log(finalScores);
// [80, 90, 100, 70]