const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, k] = input[0].split(' ').map(Number);
const scores = input[1].split(' ').map(Number);
scores.sort((a,b) => b-a);
console.log(scores[k-1]);