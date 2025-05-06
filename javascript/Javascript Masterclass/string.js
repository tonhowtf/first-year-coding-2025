'Javascript';
"Javascript";
`Javascript`;
'Javascript' === "Javascript";
'Javascript' === `Javascript`;
"Javascript" === `Javascript`;
new String('Javascript');
new String("Javascript");
new String(`Javascript`);
let counter = 0;
console.time("performance");
while (counter < 10000) {
  new String("Javascript");
  counter++;
}
console.timeEnd("performance");
let daysOfWeek = "0 - Sun\n1 - Mon \n2 - Tue\n3 - Wed\n4 - Thu\n5 - Fri\n6 - Sat ";
console.log(daysOfWeek);