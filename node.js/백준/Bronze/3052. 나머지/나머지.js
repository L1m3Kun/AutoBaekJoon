const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
let ans = new Set();

input.forEach((e) => {
    ans.add(e%42);
});

console.log(ans.size);