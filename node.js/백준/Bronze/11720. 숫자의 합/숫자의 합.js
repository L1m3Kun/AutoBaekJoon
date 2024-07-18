const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const ans = input[1].split('').map(Number).reduce((e, s) => e+s, 0);
console.log(ans);