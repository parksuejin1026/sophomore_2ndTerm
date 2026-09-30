// 열거형
var Direction;
(function (Direction) {
    Direction[Direction["Up"] = 0] = "Up";
    Direction[Direction["Down"] = 1] = "Down";
    Direction[Direction["Left"] = 2] = "Left";
    Direction[Direction["Right"] = 3] = "Right";
})(Direction || (Direction = {}));
let direction = Direction.Right;
console.log(direction); // 해당값의 인덱스 번호를 출력
var Role1;
(function (Role1) {
    Role1["Admin"] = "ADMIN";
    Role1["User"] = "USER";
    Role1["Guest"] = "GUEST";
})(Role1 || (Role1 = {}));
let userRole1 = Role1.Admin;
console.log(userRole1);
let userRole2 = Role1.Guest;
console.log(userRole2);
export {};
