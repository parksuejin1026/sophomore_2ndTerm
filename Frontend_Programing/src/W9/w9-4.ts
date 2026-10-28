// var (함수 스코프)
if (true) {
    var message1 : string = "message1";
    console.log("message1 블록 안에서 사용 : " + message1);
}

console.log("message1 블록 밖에서 사용 : " + message1);

// let, const (블록 스코프)
if (true) {
    let message2 : string = "message2";
    console.log("message2 블록 안에서 사용");
}

// console.log("message2 블록 밖에서 사용 :" + message2);
// 사용 불가능 let, const는 블록 안에서 사라짐