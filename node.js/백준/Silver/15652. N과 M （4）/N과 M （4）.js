const fs =require('fs');
const [N, M] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
const ans = [];
const solution = (start) => {
    const que = [start.toString()];
    let head = 0;
    while (head < que.length) {
        const edge = que[head];
        que[head++] = null;
        if (edge.length === M) {
            ans.push(edge.split('').join(' '));
            continue;
        }
        for (let node = Number(edge[edge.length-1]); node <= N ; node ++){
            que.push(edge+node.toString());
        }
    }
};

for (let i = 1; i <= N ; i++){
    solution(i);
}

console.log(ans.join('\n'));