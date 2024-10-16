const fs = require('fs');
const input =fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, target] = input[0].split(' ').map(Number);

const arr = input[1].split(' ').map(Number);
arr.sort((a,b) => a-b);
let ans = target;
for (let i = 0 ; i < N; i++) {
    for (let j = i+1; j < N; j++) {
        for (let k = j + 1; k < N ; k ++) {
            const res = target - arr[i] - arr[j] - arr[k];
            if (res >= 0) ans = Math.min(ans, res);
            else break;
        }
    }
}
console.log(target-ans);