const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n');
const N = Number(input[0]);
const graph = Array.from(Array(N+1), () => new Set([]));
input.slice(1).forEach((e) => {
    const [a, b] = e.split(' ').map(Number);
    graph[a].add(b);
    graph[b].add(a);
});

const visited = Array(N+1).fill(0);
const dfs = () => {
    const stack = [1];
    
    visited[1] = 1;
    while (stack.length > 0) {
        const edge = stack.pop();
        for (let node of graph[edge]){
            if (!visited[node]) {
                visited[node] = edge;
                stack.push(node);
            }
        }
    }
};
dfs();
console.log(visited.slice(2).join('\n'));
