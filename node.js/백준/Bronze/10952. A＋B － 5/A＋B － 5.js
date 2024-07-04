const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
let ans = '';
input.slice(0, -1).forEach((e) => {
    const [a, b] = e.split(' ').map(Number);
    ans += `${a+b}\n`;
})
console.log(ans);