const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n');

const n = Number(input[0]);
const tree = input.slice(1).map((e) => e.split(' ').map(Number));

const dp = Array.from(Array(n), () => new Array(n).fill(0));
dp[0][0] = tree[0][0];
for (let i = 1; i < n; i++){
    dp[i][0] = tree[i][0] + dp[i-1][0];
    for (let j = 1; j <= i ; j++){
        dp[i][j] = tree[i][j] + Math.max(dp[i-1][j], dp[i-1][j-1]); 
    }
} 

console.log(Math.max(...dp[n-1]));
