const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

console.log(input.slice(1).sort((a,b) => a-b).join('\n'));