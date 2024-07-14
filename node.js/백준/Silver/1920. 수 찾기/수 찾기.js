const fs =require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const arr = new Set(input[1].split(' ').map(Number));
const ans =[];
input[3].split(' ').map(Number).forEach((e) => {
    ans.push(arr.has(e) ? 1 : 0);
})
console.log(ans.join('\n'));