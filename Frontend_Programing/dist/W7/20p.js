class Student {
    name;
    age;
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    introduce() {
        console.log(this.name);
    }
}
export {};
