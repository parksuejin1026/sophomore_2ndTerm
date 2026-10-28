function sendRequest(method) {
    console.log(`Sending a ${method} request.`);
}
sendRequest("GET");
sendRequest("POST");
function rollDice() {
    const result = (Math.floor(Math.random() * 6) + 1);
    return result;
}
const roll = rollDice();
console.log(`주사위 던진 결과는 ${roll}`);
function toggle(active) {
    if (active) {
        console.log("불켜짐");
    }
    else {
        console.log("불꺼짐");
    }
}
toggle(true);
toggle(false);
export {};
