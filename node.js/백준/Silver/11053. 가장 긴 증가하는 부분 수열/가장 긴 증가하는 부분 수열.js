const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const A = input[1].split(' ').map(Number);
const dp = Array(1001).fill(0);
const inc = Array(1001).fill(1);

if (N >= 1) dp[0] = 1;
if (N >= 2) {
    for (let i=1 ; i< N ; i++) {
        for (let j=0 ; j<i ; j++){
            if(A[i] > A[j]) inc[i] = Math.max(inc[i],inc[j]+1);
        }
        dp[i] = Math.max(inc[i], dp[i-1]);
    }
}
console.log(dp[N-1]);