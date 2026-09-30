const scores = [65, 80, 95, 70, 90];
// find()
const firstHighScore = scores.find(score => score >= 90);
console.log(firstHighScore);
// findIndex()
const highScoreIndex = scores.findIndex(score => score >= 90);
console.log(highScoreIndex);
// filter()
const highScores = scores.filter(score => score >= 90);
console.log(highScores);
export {};
