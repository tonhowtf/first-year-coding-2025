let regExp = /^(\w+)@(\w+)(\.\w{2,3})+$/;
let result = regExp.exec("john@gmail.com.br");
console.log(result[0]);
console.log(result[1]);
console.log(result.index);
console.log(result.input);