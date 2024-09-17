const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const dp = input.slice(1,1+N).map(e=>e.split(' ').map(Number));
const ans = [];
for (let i = 0; i<N;i++){
    for (let j =1; j<N;j++){
        dp[i][j] += dp[i][j-1];        
    }
}

input.slice(1+N).forEach((e) => {
    const [x1, y1, x2, y2] = e.split(' ').map(Number);
    let total = 0;
    for (let i=x1-1;i<=x2-1;i++){
        if (y1 === 1) {
            total += dp[i][y2-1];
        } else {
            total += dp[i][y2-1]-dp[i][y1-2];            
        }
    }
    ans.push(total);
});

console.log(ans.join('\n'));
