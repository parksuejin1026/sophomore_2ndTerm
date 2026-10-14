class Student {
name: string;
age: number;
constructor(name: string, age: number) {
this.name = name;
this.age = age;
}
introduce(): string {
return `${this.name} / ${this.age}`;
}
}
const student = new Student("홍길동", 20);
console.log(student.name);
console.log(student.age);
console.log(student.introduce());