const scores = [80, 100, 70, 90, 60];
scores.sort((a, b) => b - a); // b - a 내림차순
console.log(scores);
scores.sort((a, b) => a - b); // a - b 오름차순
console.log(scores);
// 비교 함수 사용 안함
const scores2 = [80, 100, 70, 90, 60];
scores2.sort(); // 기본 문자열 비교 방식으로 정렬될 수 있음
console.log(scores2); // [ 100, 60, 70, 80, 90 ]
const scores1 = [80, 100, 70, 90, 60];
const total = scores1.reduce((sum, score) => sum + score, 0);
console.log(total);
export {};
