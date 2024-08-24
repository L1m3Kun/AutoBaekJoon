const fs = require('fs');
const input = fs.readFileSync('//dev/stdin')
                .toString()
                .trim()
                .split('\n');
const [N,M] = input[0].split(' ').map(Number);
const maze = input.slice(1);

const que = [[0,0]];
let head = 0;
const visited = Array.from(Array(N), () => new Array(M).fill(0));
visited[0][0] = 1;
const dir = [[0,1], [0,-1], [1,0], [-1,0]];

while (head < que.length) {
    const [i, j] = que[head];
    que[head++] = null;
    
    for ([di, dj] of dir) {
        const [ni, nj] = [di+i, dj+j];
        if (0 <= ni && ni < N && 0 <= nj && nj < M && maze[ni][nj] === '1' && !visited[ni][nj]){
            visited[ni][nj] = visited[i][j] + 1;
            que.push([ni,nj]);
        }
    }
}

console.log(visited[N-1][M-1]);