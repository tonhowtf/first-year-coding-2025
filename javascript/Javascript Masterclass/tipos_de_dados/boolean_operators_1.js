1 == 2;
10 === 10;
'a' != 'b';
3 !== 2;
6 > 7;
5 >= 5;
'z' < 'x';
'c' <= 'c';
0 == ''
0 == '0'
false == undefined;
false == null
null == undefined
1 == true
0 == false
0 == '\n'
0 === ''
0 === '0'
false === undefined;
false === undefined;
null === undefined
1 === true
0 === false
0 === '\n'
0 || 2;
1 || 2;
1 && 2;
0 && 2;

function generateSerial(max) {
  max = max || 1000;
  return Math.floor(Math.random() * max);
}

console.log(generateSerial(1000))
console.log(generateSerial(100))
console.log(generateSerial(10))
  (10) ? 'good' : 'bad';
(0) ? 'good' : 'bad';

