const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const campus = input.slice(1);
const findDoyeon = () => {
    for (let i = 0; i< N; i++) {
        for (let j = 0; j < M; j++){
            if (campus[i][j] === 'I') {
                return [i,j];
            }
            
        }
    }    
};

const [doI, doJ] = findDoyeon();
const direction = [[0,1], [1,0], [-1,0], [0,-1]];
const queue = {0: [doI, doJ]};
let [front, rear] = [0, 1];
let ans = 0;
const visited = Array(N).fill(0).map((e) => new Array(M).fill(0));
visited[doI][doJ] = 1;
while (front < rear){
    const [i,j] = queue[front++];
    direction.forEach(([di, dj]) => {
        const [ni, nj] = [di+i, dj+j];
        if (0 <= ni && ni < N && 0 <= nj && nj < M && visited[ni][nj]===0 && campus[ni][nj] !=='X'){
            if (campus[ni][nj] === 'O') {
                queue[rear++] = [ni, nj];
                
            } else if (campus[ni][nj] === 'P'){
                queue[rear++] = [ni, nj];
                ans ++;
            }
            visited[ni][nj] = 1;
        }
    })
}
console.log(ans > 0? ans : 'TT');