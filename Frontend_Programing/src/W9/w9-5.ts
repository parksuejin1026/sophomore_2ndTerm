function outer(): () => void {
    let message:string = "Hello";

    function inner():void {
        console.log(message);
    }

    return inner;
}

const closure: () => void = outer();

closure();