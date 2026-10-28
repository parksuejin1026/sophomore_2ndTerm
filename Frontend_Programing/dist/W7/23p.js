class Student {
    name;
    age;
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    introduce() {
        return `${this.name} / ${this.age}`;
    }
}
const student = new Student("홍길동", 20);
console.log(student.name);
console.log(student.age);
console.log(student.introduce());
export {};
