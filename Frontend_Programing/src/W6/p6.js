const book = {
    title : "프론트엔드프로그래밍",
    info : {
        category : "프로그래밍",
        price : 30000
    }
};

console.log(book.info["category"]);
console.log(book["info"].price);
console.log(book["info"]["price"]);