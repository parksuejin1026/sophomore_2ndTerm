function sayHello(name, lang) {
    return lang ? `${lang} ${name}` : `hello, ${name}!`;
}
let greet1 = sayHello("typescript", "안녕");
console.log(greet1);
let greet2 = sayHello("typescript");
console.log(greet2);
export {};
