const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

const dp = Array.from(Array(41), () => new Array(2).fill(0))
dp[0][0] = 1;
dp[1][1] = 1;

for (let i=2; i< 41; i++){
    dp[i][0] = dp[i-1][0] + dp[i-2][0];
    dp[i][1] = dp[i-1][1] + dp[i-2][1];
}

const ans = input.slice(1).map(e => dp[e].join(' '));

console.log(ans.join('\n'));