const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const n = Number(input[0]);
const arr = input[1].split(' ').map(Number);
const x = Number(input[2]);
arr.sort((a,b) => a-b);
let [i,j] = [0,n-1];

let ans = 0;

while (i < j) {
    const sum = arr[i] + arr[j];
    if (sum === x) {
        ans ++; 
        j --;
    }
    else if (sum < x) i ++;
    else j --;
} 

console.log(ans);