const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const T = Number(input[0]);
let t = 1;
let ans = [];
const dir = [[0,1], [0,-1], [-1,0], [1,0]];
while (t < input.length){
    const [M, N, K] = input[t].split(' ').map(Number);
    const bat = Array.from(Array(N), () => new Array(M).fill(0));
    const visited = Array.from(Array(N), () => new Array(M).fill(0));
    t ++;
    input.slice(t, t+K).forEach((e) => {
        const [x,y] = e.split(' ').map(Number);
        bat[y][x] = 1;
    });
    let cnt = 0;
    for (let i = 0; i< N; i++){
        for (let j = 0; j < M; j++){
            if (bat[i][j] && !visited[i][j]){
                cnt ++;
                const que = {};
                let [front, rear] = [0,0];
                que[rear++] = [i,j];
                while( front < rear ) {
                    const [ii, jj] = que[front++];
                    for ([di, dj] of dir){
                        const [ni,nj] = [ii+di, jj+dj];
                        if (0 <= ni && ni < N && 0 <= nj && nj < M && bat[ni][nj] && !visited[ni][nj]){
                            visited[ni][nj] = 1;
                            que[rear++] = [ni, nj];
                        }
                    }
                }
            }
        }
    }
    ans.push(cnt);
    t += K;
}
console.log(ans.join('\n'));