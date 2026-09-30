const apple:string = '사과';
const orange:string = '오렌지';
const pear:string = '배';
const strawberry:string = '딸기';
const num:number = 4;
// string만 들어가야 하지만 number가 들어감
const fruits:string[] = [apple, orange, pear, strawberry];
console.log(fruits);
for(let i:number=0 ; i<fruits.length ; i++){
console.log(fruits[i]);
}
