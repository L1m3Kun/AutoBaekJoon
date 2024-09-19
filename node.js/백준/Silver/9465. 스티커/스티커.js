const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const T = Number(input[0]);

const ans = [];

const solution = (n, stickers) => {
    const dp = Array.from({length: 2}, ()=>Array(n).fill(0));
    dp[0][0] = stickers[0][0];
    dp[1][0] = stickers[1][0];
    for (let j=1; j<n; j++){
        for (let i=0; i< 2; i++) {
            if (i){
                dp[i][j] = Math.max(dp[i][j-1], dp[i-1][j-1]+stickers[i][j]); 
            } else {
                dp[i][j] = Math.max(dp[i][j-1], dp[i+1][j-1]+stickers[i][j]); 
            }        
        }
    }
    ans.push(Math.max(dp[0][n-1], dp[1][n-1]));
};

let idx = 1;

while (idx < input.length){
    const n = Number(input[idx++]);
    const stickers = input.slice(idx, idx+2).map(e => e.split(' ').map(Number));
    idx += 2;
    solution(n, stickers);
}

console.log(ans.join('\n'));