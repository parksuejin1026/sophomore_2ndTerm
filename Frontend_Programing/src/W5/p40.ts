const text: string = "JavaScript";

// 문자열 길이
console.log(text.length); // 10
// 인덱스로 문자 찾기
console.log(text[0]); // J
console.log(text[3]); // a
// 마지막 문자 찾기
console.log(text[text.length - 1]); // t
console.log(text.at(-1)); // t
// 문자 또는 문자열 찾기
console.log(text.includes("Script")); // true 문자가 포함
console.log(text.indexOf("a")); // 1 인덱스 위치
console.log(text.lastIndexOf("a")); // 3 마지막 인덱스 위치