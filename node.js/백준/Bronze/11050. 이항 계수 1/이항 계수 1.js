const fs = require('fs');
const [N, K] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);

const dp = Array(N+1).fill(0).map(() => new Array(K+1).fill(0));
for (let i=0;i<=N;i++){
    for (let j=0;j<=Math.min(i, K);j++){
        if (j === 0 || j === i){
            dp[i][j] = 1;
        } else {
            dp[i][j] = dp[i-1][j-1]+ dp[i-1][j];
        }
    }
}
console.log(dp[N][K]);