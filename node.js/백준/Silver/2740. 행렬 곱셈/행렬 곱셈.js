const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const matrixA = input.slice(1, N+1).map(str => str.split(' ').map(Number));
const [_, K] = input[N+1].split(' ').map(Number);
const matrixB = input.slice(N+2).map(str => str.split(' ').map(Number));

const answer = Array.from({length: N}, ()=>Array(K).fill(0));

for(let i = 0; i<N;i++){
    for (let k = 0; k < K; k++){
        for (let j =0 ;j < M; j++){
            answer[i][k] += matrixA[i][j] * matrixB[j][k]   
        }
    }
}
answer.forEach((e) => {
    console.log(...e);
})