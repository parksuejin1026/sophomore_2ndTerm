const student: [string, number] = ["홍길동", 20];
const [studentName, studentAge] = student;
console.log(studentName); // 홍길동
console.log(studentAge); // 20

function getUser(): [string, number] {
    return ["홍길동", 20];
}
const [userName, userAge] = getUser();
console.log(userName); // 홍길동
console.log(userAge); // 20

// 연습해보기
function getUser2(name : string, num : number) : [string, number] {
    return [name, num];
}
const [userName2, userAge2] = getUser2("박수진", 25);
console.log(userName2);
console.log(userAge2);