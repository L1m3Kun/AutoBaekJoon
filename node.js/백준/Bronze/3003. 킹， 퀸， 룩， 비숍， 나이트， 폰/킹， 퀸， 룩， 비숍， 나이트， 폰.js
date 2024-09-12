const fs =require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
const standard = [1, 1, 2, 2, 2, 8];
const ans = input.map((e,i) => standard[i]-e);
console.log(ans.join(' '));