let id: string | number; // string 또는 number
id = 100;
id = "A100";
function printId(id: string | number) {
console.log(id);
}
id = 100;
printId(id);
id = "A100";
printId(id);