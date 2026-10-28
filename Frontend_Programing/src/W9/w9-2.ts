// 두 숫자를 더하는 함수

function add(a: number, b: number): number {
    return a + b;
}

// add 함수의 반환 타입 추출
type ResultType = ReturnType<typeof add>;

// ResultType은 number 타입
let result:ResultType = add(10, 20);

console.log(result);
