const fs = require('fs');
let [N, K] = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split(' ')
                .map(Number);

let ans = 0;
if (N > K) {
    ans = N - K;
} else if (N < K) {
    const dp = Array(100001).fill(100001);
    dp[N] = 0;
    const que = [N];
    let front = 0;
    while (front < que.length) {
        const edge = que[front];
        que[front++] = null;
        
        for (const node of [edge<<1, edge+1, edge-1]){
            if (0<= node && node < 100001 && dp[edge]+1 < dp[node]) {
                dp[node] = dp[edge]+1;
                que.push(node);
            }
        }
    }
    ans = dp[K];
} 
console.log(ans);