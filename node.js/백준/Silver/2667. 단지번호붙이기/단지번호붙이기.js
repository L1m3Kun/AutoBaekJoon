const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n');

const N = Number(input[0]);
const visited = Array.from(Array(N), () => new Array(N).fill(0));
const ans = [];
const dir = [[0,1], [0,-1], [1,0], [-1,0]];
const apartment = input.slice(1);
for (let i = 0 ; i < N ; i++){
    for (let j = 0; j< N; j++){
        if (apartment[i][j] === '1' && !visited[i][j]){
            visited[i][j] = 1;
            let complex = 1;
            const que = {};
            let [front, rear] = [0,0];
            que[rear++] = [i,j];
            while (front < rear) {
                const [y, x] = que[front];
                que[front++] = null;
                for (let [di, dj] of dir){
                    const [ni, nj] = [di+y, dj+x];
                    if (0 <= ni && ni <N && 0 <= nj && nj < N && apartment[ni][nj] === '1' && !visited[ni][nj]){
                        visited[ni][nj] = 1;
                        que[rear++] = [ni,nj];
                        complex ++;
                    }
                }
            }
            ans.push(complex);
        }
        
    }
}

ans.sort((a,b) => a-b);
console.log([ans.length,...ans].join('\n'));
