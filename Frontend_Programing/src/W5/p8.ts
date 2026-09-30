const score: number = 85;
const level: number = Math.floor(score / 10);
let grade: string;
switch (level) {
case 10:
case 9:
grade = "A";
break;
case 8:
grade = "B";
break;
default:
grade = "C";
}
console.log(grade); // B
