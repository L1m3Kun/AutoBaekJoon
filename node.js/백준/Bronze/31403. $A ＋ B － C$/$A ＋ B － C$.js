const fs = require('fs');
const [a, b, c] = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n');

const ans = [];
ans.push(Number(a) + Number(b) - Number(c));
ans.push(Number(a+b)- Number(c));

console.log(ans.join('\n'));