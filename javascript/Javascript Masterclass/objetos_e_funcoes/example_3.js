const functionalLanguage = Object.create({});
functionalLanguage.paradigm = "Functional";
const scheme = Object.create(functionalLanguage);
scheme.name = "Scheme";
scheme.year = 1975;
const javascript = Object.create(functionalLanguage);
javascript.name = "Javascript";
javascript.year = 1995;
javascript.paradigm = "OO";

console.log(javascript);
console.log(javascript.paradigm);
console.log(javascript.__proto__.paradigm);
console.log(Object.getPrototypeOf(javascript).paradigm);