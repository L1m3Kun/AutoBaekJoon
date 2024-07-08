const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const ans = [];

input.slice(0,input.length-1).forEach((e) => {
   const [a, b, c] = e.split(' ').map(Number).sort((a,b) => a-b);
   if (a**2 + b**2 === c**2) ans.push('right');
    else ans.push('wrong');
});

console.log(ans.join('\n'));