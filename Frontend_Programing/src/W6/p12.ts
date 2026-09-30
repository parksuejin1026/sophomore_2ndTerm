const students = [ // 배열에 객체 생성
    { name: "홍길동" },
    { name: "김철수" }
];
const reference = students;
console.log(students === reference); // true
reference[0].name = "이영희";
console.log(students[0].name); // 이영희
