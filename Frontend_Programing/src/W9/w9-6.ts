type Counter = {
    increase: () => void;
    decrease: () => void;
    show: () => void;
};
const counter = function (): Counter {
let count: number = 0;
function changeCount(number: number): void {
    count += number;
    }
    return {
        increase: function (): void {
        changeCount(1);
    },
    decrease: function (): void {
    changeCount(-1);
    },
        show: function (): void {
        console.log(count);
        },
    };
};
const counterClosure: Counter = counter();
counterClosure.increase();
counterClosure.show(); // 1
counterClosure.decrease();
counterClosure.show(); // 0
