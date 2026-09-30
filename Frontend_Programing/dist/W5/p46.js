// forEach 함수에서 첫 번째는 요소 두 번째는 인덱스 번호 세 번쨰는 배열 전체 출력
function printNames(namesArr) {
    namesArr.forEach((name, index, arr) => console.log(name + " : " + index + "=> " + arr));
}
printNames(["kim", "lee", "park"]);
// 익명 함수로 콜백함수 생성
const arr = ["가", "나", "다"];
arr.forEach(function (element) {
    console.log(element);
});
export {};
