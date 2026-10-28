const counter = function () { // 외부 함수 Counter()
    let count = 0; // 외부 함수의 지역 변수
    function changeCount(number) { // 내부 함수 changeCount()
        count += number; // 외부 함수의 변수 접근
    }

    return { // increase , decrease, show 내부함수 선언한 객체 반환
        increase: function () {
            changeCount(1);
        },
        decrease: function () {
            changeCount(-1);
        },
        show: function () {
            console.log(count);
        },
    };
};
// counter() 실행, count = 0, 내부 함수(increase() , decrease() , show() )들이 포함된 객체 반환
// 이 함수들은 counter()의 count에 접근할 수 있음
const counterClosure = counter(); // counter() 호출 후 객체 반환 후 counter() 함수 실행 종료

counterClosure.increase();
counterClosure.show(); // 1

counterClosure.decrease();
counterClosure.show(); // 0
