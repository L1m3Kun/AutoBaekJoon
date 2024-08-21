const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n');
const N = Number(input[0]);
const arr = input[1].split(' ').map(Number);
const idx = {};
const ans = Array(N).fill(0);

arr.forEach((e,i) => {
    if (e in idx) {
        idx[e].push(i);
    } else {
        idx[e] = [i];
    }
});

Object.keys(idx)
      .sort((a,b) => a-b)
      .forEach((e,i) => {
         for (let index of idx[e]){
             ans[index] = i;
         }   
      });

console.log(ans.join(' '));
