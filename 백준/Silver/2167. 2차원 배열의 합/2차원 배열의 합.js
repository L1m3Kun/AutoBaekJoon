const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');

const [N, M] = input[0].split(" ").map(Number);
const matrix = input.slice(1, N+1).map((e) => e.split(" ").map(Number));
const testCase = input.slice(N+2, -1).map((e)=> e.split(" ").map(Number));
const prefix = Array.from({length: N+1}, () => Array(M+1).fill(0));
const answer = [];

for(let r = 1; r <= N; r++){
    for (let c = 1; c <= M; c++){
        prefix[r][c] = prefix[r][c-1] + prefix[r-1][c] - prefix[r-1][c-1] + matrix[r-1][c-1];
    }
}

testCase.forEach(([i, j, x, y]) => {
    answer.push(prefix[x][y] - prefix[x][j-1] - prefix[i-1][y] + prefix[i-1][j-1]);
});
console.log(answer.join("\n"));