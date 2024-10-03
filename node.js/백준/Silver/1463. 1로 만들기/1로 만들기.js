const fs = require('fs');
const N = Number(fs.readFileSync('/dev/stdin').toString().trim());

const dp = Array(N+1).fill(1000001);
dp[N] = 0;

for (let num = N; num > 0; num --){
    if (!(num % 3)) dp[num / 3] = Math.min(dp[num]+1, dp[num/3]);
    if (!(num & 1)) dp[num >> 1] = Math.min(dp[num]+1, dp[num>>1]);
    dp[num-1] = Math.min(dp[num-1], dp[num]+1);
}
console.log(dp[1]);