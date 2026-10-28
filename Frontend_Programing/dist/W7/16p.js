const user = {
    username: "동미대"
};
console.log(user.username); // 동미대
console.log(user.email); // undefined
// 선택적 속성에 값 추가
user.email = "abc@mail.com";
console.log(user.email); // abc@mail.com
const account = {
    username: "동미대",
    email: "abc@mail.com",
};
console.log(account.username);
console.log(account.email);
// 일반 속성 변경
account.email = "new@mail.com";
console.log(account.email);
export {};
// readonly 속성 변경
// account.username = "홍길동"; // 오류: username은 읽기 전용 속성
