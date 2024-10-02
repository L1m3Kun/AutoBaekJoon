const fs = require('fs');
const input =fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, S] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number);

let ans = 100001;
let [i, j] = [0, 0];
let sum = 0;
while (j < N) {
    sum += arr[j];
    while ( sum >= S) {
        ans = Math.min(ans, j-i+1);
        sum -= arr[i++];
    }
    j++;
}

console.log(ans === 100001 ? 0 : ans);