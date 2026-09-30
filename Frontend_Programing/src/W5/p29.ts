// 1차원 배열
const scores: number[] = [80, 90, 70];
for (let i: number = 0; i < scores.length; i++) {
console.log(scores[i]);
}
// 2차원 배열
const studentScores: number[][] = [
[80, 90, 70],
[90, 85, 95],
[70, 80, 75]
];
// 중첩 반복문으로 출력
for (let i: number = 0; i < studentScores.length; i++) {
console.log(`${i + 1}번 학생`);
for (let j: number = 0; j < studentScores[i].length; j++) {
console.log(studentScores[i][ j]);
}
}