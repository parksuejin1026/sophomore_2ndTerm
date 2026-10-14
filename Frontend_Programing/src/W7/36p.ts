// 문자열 리터럴
type RequestMethod = "GET" | "POST" | "PUT" | "DELETE";
function sendRequest(method:RequestMethod){
console.log(`Sending a ${method} request.`);
}
sendRequest("GET");
sendRequest("POST");
//sendRequest("FETCH"); //error TS2345: Argument of type '"FETCH"' is not assignable to parameter of type 'RequestMethod'.

// 숫자 리터럴
type DiceRoll = 1 | 2 | 3 | 4 | 5 | 6;
function rollDice(): DiceRoll {
const result = (Math.floor(Math.random() * 6) + 1) as DiceRoll;
return result;
}
const roll = rollDice();
console.log(`주사위 던진 결과는 ${roll}`);

// 불리언 리터럴
type IsActive = true | false;
function toggle(active: IsActive) {
if(active) {
console.log("불켜짐");
} else {
console.log("불꺼짐");
}
}
toggle(true);
toggle(false);
