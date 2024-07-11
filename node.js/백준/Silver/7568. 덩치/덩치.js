const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const N = Number(input[0]);
const arr = input.slice(1).map((e) => {
    return e.split(' ').map(Number);
});

const ans = Array(N).fill(1);
arr.forEach((e, i) => {
    for (let j=0;j<N;j++){
        if (e[0] < arr[j][0] && e[1] < arr[j][1]){
            ans[i] ++;
        }
    }
});
console.log(...ans);