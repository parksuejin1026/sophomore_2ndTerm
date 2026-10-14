class Person {
public name: string;
protected age: number;
private password: string;
constructor(
name: string,
age: number,
password: string
) {
this.name = name;
this.age = age;
this.password = password;
}
showInfo(): void {
// 클래스 내부에서는 모두 접근 가능
 console.log(this.name);
console.log(this.age);
console.log(this.password);
}
}
class Student extends Person {
showStudent(): void {
console.log(this.name);
 console.log(this.age);
 // console.log(this.password); // 자식클래스 접근 오류
 }
}
const student = new Student("홍길동", 20, "1234");
// public → 외부에서 접근 가능
console.log(student.name);
// protected → 외부에서 접근 불가
// console.log(student.age); // 오류
// private → 외부에서 접근 불가
// console.log(student.password); // 오류
student.showInfo();
student.showStudent();