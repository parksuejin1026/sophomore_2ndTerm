const scores: number[][] = [
    [80, 90],
    [100, 80],
    [90, 70]
];

// 1. 중첩 배열을 1차원 배열로 변환
const flatScores: number[] = scores.flat();
console.log(flatScores);
// 2. 배열을 특정 값으로 채우기
const result: number[] = new Array(5).fill(0);
console.log(result);
// 3. Set으로 중복 제거
const uniqueScores: Set<number> = new Set(flatScores);
console.log(uniqueScores);
console.log(uniqueScores.size);
// 4. Set을 다시 배열로 변환
const finalScores: number[] = Array.from(uniqueScores);
console.log(finalScores);