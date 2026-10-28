class Student {
    name;
    constructor(name) {
        this.name = name;
    }
    introduce() {
        console.log(`안녕하세요. ${this.name}입니다.`);
    }
}
const student = new Student("홍길동");
student.introduce();
export {};
