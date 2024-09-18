const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, K] = input[0].split(' ').map(Number);
const items = input.slice(1).map(e=>e.split(' ').map(Number));
const dp = Array.from({length: N+1}, () => Array(K+1).fill(0));

for (let i = 1; i<N+1; i++) {
    for (let j= 1 ; j <= K; j++) {
        if (j < items[i-1][0]) {
            dp[i][j] = dp[i-1][j];
        } else {
            dp[i][j] = Math.max(dp[i-1][j], dp[i-1][j-items[i-1][0]]+items[i-1][1]);
        }
    }
}
console.log(dp[N][K]);