const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().length;
console.log(input);