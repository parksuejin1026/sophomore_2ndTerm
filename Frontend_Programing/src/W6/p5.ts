const book: { // book 객체 생성
    title: string; // 제목 문자열
    author: string; // 저자 문자열
    year: number; // 출판년도 숫자
    publisher?: string; // 출판사(없어도 무방) 문자열
} = {
    title: "프론트앤드프로그래밍",
    author: "동미대",
    year: 2026
};

// 1. 객체 속성 접근 - 마침표(.) 사용
console.log(book.title); // 프론트앤드프로그래밍
console.log(book.author); // 동미대
console.log(book.year); // 2026

// 대괄호([]) 사용
console.log(book["title"]); // 프론트앤드프로그래밍
console.log(book["author"]); // 동미대

// 2. 객체 속성 추가하기
book.publisher = "DMU출판사";
console.log(book.publisher); // DMU출판사

// 3. 객체 속성 수정하기
book.author = "홍길동";
book.year = 2027;
console.log(book.author); // 홍길동
console.log(book.year); // 2027
// 4. 객체 속성 삭제하기
delete book.publisher
;
console.log(book.publisher); // undefined
