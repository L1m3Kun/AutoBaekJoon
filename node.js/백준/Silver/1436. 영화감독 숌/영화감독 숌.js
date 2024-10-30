const fs = require('fs');
const n = Number(fs.readFileSync('/dev/stdin').toString().trim());

const has666 = (num) => num.toString().includes('666') ? true : false
let cnt = 0;
let i = 1;
while (cnt !== n) {
    i++;
    if (has666(i)) cnt ++;
}
console.log(i)