const fs = require('fs');
const [N, M] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
const ans = [];

const bf = (start) => {
    const que = [start.toString()];
    let head = 0;
    while (head < que.length) {
        const edge = que[head];
        que[head++] = null;
        if (edge.length >= M){
            ans.push(edge.split('').join(' '));
            continue;
        }
        for (let i = Number(edge[edge.length-1])+1; i <= N; i++) {
            que.push(edge+i.toString());
        }
    }
}
for (let s = 1; s <= N ; s++ ){
    bf(s);
}
console.log(ans.join('\n'));