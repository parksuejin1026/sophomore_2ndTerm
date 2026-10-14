interface Person {
name: string;
introduce(): void;
}
class Student implements Person {
name: string;
constructor(name: string) {
this.name = name;
}
introduce(): void {
console.log(`안녕하세요. ${this.name}입니다.`);
}
}
const student = new Student("홍길동");
student.introduce();
