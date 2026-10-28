type UserCallback = ( // 콜백함수 리턴 타입 지정
  error: Error | null, // Error이거나 값이 없음
  userName?: string // 사용자이름이 있다면 string
) => void; // 리턴 자체는 void

function getUser(callback: UserCallback): void { // 리턴값이 나오지 않는 getUser 함수 매개변수는 콜백함수고 타입은 위에 지정했던 타입
  console.log("사용자 데이터 요청"); // 처음 데이터 요청 출력

  setTimeout((): void => {
    const success: boolean = true; // 일단 success 는 true

    if (success) { // true기 때문에 
      callback(null, "홍길동"); // 콜백함수의 매개변수였던 error와 userName 인수로 지정
    } else {
      callback(new Error("사용자 데이터 조회 실패")); // false면
    }
  }, 1000);
}

getUser((error: Error | null, userName?: string): void => {
  if (error) {
    console.log(error.message);
    return;
  }

  console.log(`사용자 이름: ${userName}`);
});