const book: {
    title: string;
    author: string;
    year: number;
// 중첩 객체
    info: {
        category: string;
        price: number;
        };
// 선택적 속성
    publisher?: {
        name: string;
        address?: string;
        };
// 메서드
getBookInfo: () => string; 
} = {
    title: "프론트앤드프로그래밍",
    author: "동미대",
    year: 2026,
    info: {
        category: "프로그래밍",
        price: 30000
        },
getBookInfo: function () {
    return `${this.title} / ${this.author}`;    
    }
};

// 1. 중첩 객체의 속성 접근
console.log(book.info.category); // 프로그래밍
console.log(book["info"]["price"]); // 30000
// 마침표와 대괄호 조합
console.log(book.info["category"]); // 프로그래밍
console.log(book["info"].price); // 30000
// 2. ?.(옵셔널 체이닝) : 자바스크립트, 타입스크립트 모두 사용
console.log(book.publisher?.name); // undefined
console.log(book.publisher?.address); // undefined
// 3. 객체의 메서드 호출
console.log(book.getBookInfo());
// 프론트앤드프로그래밍 / 동미대

// 4. 객체간 비교
const book2 = {
title: "프론트앤드프로그래밍",
author: "동미대",
year: 2026
};
const book3 = book;
console.log(book === book2); // false
console.log(book === book3); // true