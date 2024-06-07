const fs = require("fs");

const settings = () => {
    // const input = fs.readFileSync("input.txt").toString().trim().split("\n");
    const input = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
    const [N, M, V] = input[0].split(" ").map(Number);
    const graph = [];
    for (let i =0;i<=N;i++){
        graph.push([]);
    }
    input.slice(1,).forEach(e => {
        const [start,end] = e.split(" ").map(Number);
        graph[start].push(end);
        graph[end].push(start);
    })
    // console.log(graph)
    return [N, V,graph];
}

const main = (N, start, graph) => {
    const dfs = (start) => {
        const visited = Array(N+1).fill(0);
        const answer = [];
        const stack = [start];
        // visited[start] = 1;
        while (stack.length > 0) {
            // console.log(stack);
            const spot = stack.pop();
            if (visited[spot]) continue;
            visited[spot] = 1
            answer.push(spot);
            graph[spot].sort((a,b) => b-a);
            for (let node of graph[spot]) {
                // if (!visited[node]){
                    // visited[node] = 1;
                stack.push(node);
                // }
            }
        }
        console.log(...answer);
    }

    const bfs = (start) => {
        const visited = Array(N+1).fill(0);
        const answer = [];
        const queue = {};
        let [front, rear] = [0, 0];
        queue[rear++] = start;
        visited[start] = 1;
        while (rear - front > 0) {
            const spot = queue[front++];
            answer.push(spot);
            graph[spot].sort((a,b) => a-b);
            for (let node of graph[spot]) {
                if (!visited[node]) {
                    visited[node] = 1;
                    queue[rear++] = node;
                }
            }
        }
        console.log(...answer);
    }

    dfs(start);
    bfs(start);
}

const [N ,start, graph] = settings();
main(N, start, graph);