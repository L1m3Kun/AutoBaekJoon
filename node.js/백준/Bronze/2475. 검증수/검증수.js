const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);

const result = input.reduce((acc, curr) => acc + curr**2, 0);

console.log(result%10);