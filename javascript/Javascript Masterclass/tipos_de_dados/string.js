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
let host = "localhost";
let port = "3000";
let resource = "users";
let url = "https://" + host + ":" + port + "/" + resource;
console.log(url)
let url2 = `https://${host}:${port}/${resource}`;
console.log(url2)
