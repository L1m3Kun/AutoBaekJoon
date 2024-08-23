const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n');

const [N, M] = input[0].split(' ').map(Number);
const graph = Array.from(Array(N+1), () => []);

input.slice(1).forEach((e) => {
    const [u, v] = e.split(' ').map(Number);
    graph[u].push(v);
    graph[v].push(u);
});

const parent = Array(N+1).fill(0).map((_,i) => i);

const find = (num) => {
    while (num !== parent[num]){
        num = parent[num];
    }
    return parent[num];
}

const union = (num1, num2) => {
    const f1 = find(num1);
    const f2 = find(num2);
    
    if (f1 !== f2) parent[num2] = f1;
}
const visited = Array(N+1).fill(0);
for (let i =1; i <= N; i++){
    if (visited[i]) continue
    const que = {};
    let [front, rear] = [0,0];
    que[rear++] = i;
    visited[i] = 1;
    while (front < rear) {
        const edge = que[front];
        que[front++] = null;
        for ( let node of graph[edge] ){
            if (!visited[node]){
                visited[node] = 1;
                union(edge, node);
                que[rear++] = node;
            }
        }
    }
}

const ans = new Set(parent.slice(1));
console.log(ans.size);
                