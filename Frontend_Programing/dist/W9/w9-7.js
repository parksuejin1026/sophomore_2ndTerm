function getUser(callback) {
    console.log("사용자 데이터 요청"); // 처음 데이터 요청 출력
    setTimeout(() => {
        const success = true; // 일단 success 는 true
        if (success) { // true기 때문에 
            callback(null, "홍길동"); // 콜백함수의 매개변수였던 error와 userName 인수로 지정
        }
        else {
            callback(new Error("사용자 데이터 조회 실패")); // false면
        }
    }, 1000);
}
getUser((error, userName) => {
    if (error) {
        console.log(error.message);
        return;
    }
    console.log(`사용자 이름: ${userName}`);
});
export {};
