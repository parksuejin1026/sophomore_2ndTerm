function outer() {
    let message = "Hello";
    function inner() {
        console.log(message);
    }
    return inner;
}
const closure = outer();
closure();
export {};
