const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

const ans = input.slice(1).sort((a,b) => a-b);
console.log(ans.join('\n'));