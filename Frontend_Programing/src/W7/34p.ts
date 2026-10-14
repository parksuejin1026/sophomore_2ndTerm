// 타입 별칭
type ID = string | number;
let userId: ID;
userId = "id1234";
console.log(userId);
userId = 123456;
console.log(userId);
//userId = true; // error TS2322: Type 'boolean' is not assignable to type 'ID'.
console.log(userId);

// 함수 타입 별칭 적용
type Operation = (x:number, y:number) => number;
const plus: Operation = (a, b) => a+b;
const minus: Operation = (a, b) => a-b;
console.log(plus(5,3));
console.log(minus(10,7));

// 객체 타입 별칭 적용
type User = {
name: string;
age: number;
email?:string;
};
const user1:User = {
name:"kim",
age:25
};
const user2:User = {
name:"lee",
age:30,
email:"abc@mail.com"
};
console.log(user1);
console.log(user2);

// 타입 별칭과 인터페이스 결합
type MyLocation = {
country: string;
city: string;
zipCode: string;
};
interface Company {
name: string;
employee: number;
location: MyLocation;
}
const company: Company = {
name: "코딩연구소",
employee: 5,
location:{
country:"대한민국",
city:"서울",
zipCode:"12345",
},
};
console.log(company);
