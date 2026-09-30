const scores: number[] = [80, 90, 70, 100];
const result: boolean = scores.every(
score => score >= 60
);
console.log(result);


const scores1: number[] = [50, 60, 70, 95];
const result1: boolean = scores.some(
score => score >= 90
);
console.log(result);