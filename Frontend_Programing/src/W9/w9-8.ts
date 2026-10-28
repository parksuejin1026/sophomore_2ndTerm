function getUser(): Promise<string> {
    return new Promise<string>( (resolve, reject) => {
    console.log("사용자 데이터 요청");
    setTimeout((): void => {
        const success: boolean = true;
        if (success) {
            resolve("홍길동");
        } else {
                reject(new Error("사용자 데이터 조회 실패"));
            }
        }, 1000);
    });
}
getUser()
    .then((userName: string): void => {
    console.log(`사용자 이름: ${userName}`);
    })
    .catch((error: unknown): void => {
    if (error instanceof Error) {
        console.log(error.message);
    }
});