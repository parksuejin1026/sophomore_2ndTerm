class Student {
    name;
    age;
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    introduce() {
        console.log(`이름: ${this.name}, 나이: ${this.age}`);
    }
}
const student1 = new Student("홍길동", 20);
const student2 = new Student("김철수", 21);
student1.introduce();
student2.introduce();
export {};
