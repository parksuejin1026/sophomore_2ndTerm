// 열거형
enum Direction {
    Up,
    Down,
    Left,
    Right
}
let direction: Direction = Direction.Right;
console.log(direction); // 해당값의 인덱스 번호를 출력

enum Role1 {
    Admin = "ADMIN",
    User = "USER",
    Guest = "GUEST" 
}

let userRole1: Role1 = Role1.Admin;
console.log(userRole1);
let userRole2: Role2 = Role1.Guest;
console.log(userRole2);
type Role2 = "ADMIN" | "USER" | "GUEST";