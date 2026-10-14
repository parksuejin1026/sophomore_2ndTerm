interface Calculator{
plus(a:number, b:number): number;
minus(a:number, b:number): number;
}
const myCalculator: Calculator = {
plus(a,b) { // a,b 타입선언은 Calculator에서 선언해서 생략
return a+b;
},
minus(a,b) {
return a-b;
}
};
console.log(myCalculator.plus(10,5));
console.log(myCalculator.minus(10,5));

interface Person {
name:string;
age:number;
}
interface Employee extends Person {
employeeId:number;
}
const employee: Employee = {
name: "동미대",
age: 21,
employeeId: 5555
};
console.log(employee.name);
console.log(employee.age);
console.log(employee.employeeId);
