function getUser() {
    return new Promise((resolve, reject) => {
        console.log("사용자 데이터 요청");
        setTimeout(() => {
            const success = true;
            if (success) {
                resolve("홍길동");
            }
            else {
                reject(new Error("사용자 데이터 조회 실패"));
            }
        }, 1000);
    });
}
async function main() {
    try {
        const userName = await getUser();
        console.log(`사용자 이름: ${userName}`);
    }
    catch (error) {
        if (error instanceof Error) {
            console.log(error.message);
        }
    }
}
main();
export {};
