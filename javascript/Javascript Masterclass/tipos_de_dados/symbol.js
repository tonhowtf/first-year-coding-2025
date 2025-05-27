Symbol("a");
Symbol("b");
Symbol("c");
Symbol.hasInstance
Symbol.isConcatSpreadable
Symbol.iterator
Symbol.match
Symbol.replace
Symbol.search
Symbol.species
Symbol.split
Symbol.toPrimitive
Symbol.toStringTag
Symbol.unscopables
let regexp = /Javascript/
regexp[Symbol.match] = false
console.log("/Javascript/".startsWith(regexp));