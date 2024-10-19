const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
console.log(Math.floor(input.reduce((prev, now) => prev+now, 0) / input.length));
input.sort((a,b) => a-b);
console.log(input[input.length >> 1]);