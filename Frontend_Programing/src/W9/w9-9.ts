function getUser(): Promise<string> {
  return new Promise<string>((resolve, reject) => {
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

async function main(): Promise<void> {
  try {
    const userName: string = await getUser();
    console.log(`사용자 이름: ${userName}`);
  } catch (error: unknown) {
    if (error instanceof Error) {
      console.log(error.message);
    }
  }
}

main();