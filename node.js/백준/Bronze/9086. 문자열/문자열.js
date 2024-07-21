const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const ans = input.slice(1).map((e) => e[0]+e[e.length-1])
console.log(ans.join('\n'));