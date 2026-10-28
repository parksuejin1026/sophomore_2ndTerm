let userId;
userId = "id1234";
console.log(userId);
userId = 123456;
console.log(userId);
//userId = true; // error TS2322: Type 'boolean' is not assignable to type 'ID'.
console.log(userId);
const plus = (a, b) => a + b;
const minus = (a, b) => a - b;
console.log(plus(5, 3));
console.log(minus(10, 7));
const user1 = {
    name: "kim",
    age: 25
};
const user2 = {
    name: "lee",
    age: 30,
    email: "abc@mail.com"
};
console.log(user1);
console.log(user2);
const company = {
    name: "코딩연구소",
    employee: 5,
    location: {
        country: "대한민국",
        city: "서울",
        zipCode: "12345",
    },
};
console.log(company);
export {};
