const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [n, m] = input[0].split(' ').map(Number);
const field = input.slice(1).map(e => e.split(' ').map(Number));
const dir = [[0,1], [0,-1], [1,0], [-1,0]];

const visited = Array.from(Array(n), () => new Array(m).fill(-1));
const que = {};
let [front, rear] = [0,0];


for (let i = 0; i < n; i++) {
    for (let j=0; j < m; j++) {
        if (field[i][j] === 2) {
            que[rear++] = [i,j];
            visited[i][j] = 0;
        } else if (field[i][j] === 0){
            visited[i][j] = 0;
        }
    }
}

while (front < rear) {
    const [i,j] = que[front++];
    for ([di, dj] of dir) {
        const [ni, nj] = [di+i, dj+j];
        if (0 <= ni && ni < n && 0 <= nj && nj < m){
            if (visited[ni][nj] === -1 && field[ni][nj] !== 0){
                visited[ni][nj] = visited[i][j] + 1;
                que[rear++] = [ni, nj];
            }
        }
    }    
}
const ans = visited.map(e => e.join(' '));
console.log(ans.join('\n'));

