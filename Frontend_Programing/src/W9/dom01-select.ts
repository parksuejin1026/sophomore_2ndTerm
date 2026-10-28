const title = document.querySelector<HTMLHeadingElement>("#title");
const message = document.querySelector<HTMLParagraphElement>(".message");
console.log('title : ' + title);
console.log('message : '+ message);
window.alert(`title : ${title}`);
window.alert(`message : ${message}`);