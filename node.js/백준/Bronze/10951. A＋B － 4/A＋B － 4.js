const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const ans = [];
input.forEach((e) => {
    const [a, b] = e.split(' ').map(Number);
    ans.push(a+b);
})
console.log(ans.join('\n'));