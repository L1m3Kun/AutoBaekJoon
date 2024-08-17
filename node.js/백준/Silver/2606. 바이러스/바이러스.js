const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n')

const N = Number(input[0]);
const M = Number(input[1]);
const network = {};
input.slice(2).forEach((e) => {
    const [a, b] = e.split(' ').map(Number);
    if (a in network) {
        network[a].add(b);
    } else {
        network[a] = new Set([b]);
    }
    if (b in network) {
        network[b].add(a);
    } else {
        network[b] = new Set([a]);
    }
});

const que = {};
let [front, rear] = [0,0];
que[rear++] = 1;
let ans = 0;
const visited = Array(N+1).fill(0);
visited[1] = 1;
while (front < rear) {
    const edge = que[front];
    que[front++] = null;
    if (!(edge in network)) continue;
    for (let node of network[edge]){
        if (!visited[node]) {
            visited[node] = 1;
            ans ++;
            que[rear++] = node;
        }
    }
}
console.log(ans);