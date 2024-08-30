const fs = require('fs');
const [N, K] = fs.readFileSync('/dev/stdin')
                 .toString()
                 .trim()
                 .split(' ')
                 .map(Number);

const dp = Array.from(Array(100001), () => [100001, 0]);
const que = [N];
let head = 0;
dp[N] = [0, 1]
while (head < que.length) {
    const edge = que[head];
    que[head++] = null;
    for (let node of [edge << 1, edge + 1, edge - 1]) {
        if (node < 100001 && 0 <= node) {
            if (dp[edge][0] + 1 < dp[node][0]) {
                dp[node] = [dp[edge][0]+1, 1];
                que.push(node);
            } else if (dp[edge][0] + 1 === dp[node][0]) {
                dp[node][1] ++;
                que.push(node);
            }
        }
    }
}
console.log(dp[K].join('\n'));