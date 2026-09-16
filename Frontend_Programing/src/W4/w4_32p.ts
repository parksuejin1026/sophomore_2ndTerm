interface User {
    name : string;
    age : number;
}

const user: User = {
    name : "Kim",
    age : 20
};

interface User1 {
    name : string;
    age : number;
    email ?: string; // 선택적 속성
}

const user1: User1 = {
    name : "kim",
    age : 20
};

const user2 : User1 = {
    name : "park",
    age : 20,
    email : "parksuejin@naver.com"
};

interface User2 {
    readonly id : number;
    name : string;
}

const user3 : User2 = {
    id: 1,
    name : "Lee"
};

user3.name = "Lee";
// user.id = 2; // readonly라 불가능