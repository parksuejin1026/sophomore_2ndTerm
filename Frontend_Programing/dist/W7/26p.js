class Person {
    static species = "Human"; // static 속성
    name;
    constructor(name) {
        this.name = name;
    }
    introduce() {
        console.log(`안녕하세요. 저는 ${this.name}입니다.`);
    }
    static showSpecies() {
        console.log(`종류: ${Person.species}`);
    }
}
// Student가 Person을 상속
class Student extends Person {
    major;
    constructor(name, major) {
        // 부모 클래스의 constructor 호출
        super(name);
        this.major = major;
    }
    // 메서드 오버라이딩
    introduce() {
        console.log(`안녕하세요. 저는 ${this.name}이고, 전공은
${this.major}입니다.`);
    }
    study() {
        console.log(`${this.name}이 공부합니다.`);
    }
}
const student = new Student("홍길동", "인공지능소프트웨어");
// 상속받은 속성 사용
console.log(student.name);
// 자식 클래스의 속성 사용
console.log(student.major);
// 오버라이딩된 메서드 호출
student.introduce();
// 자식 클래스의 메서드 호출
student.study();
// static은 객체가 아니라 클래스에서 호출
Person.showSpecies();
console.log(Person.species);
export {};
