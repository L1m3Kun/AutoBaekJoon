const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [n, m, v] = inputs[0].split(" ").map(Number);
const tree = inputs.slice(1).reduce(
  (tree, input) => {
    const [l, r] = input.split(" ").map(Number);
    tree[l].push(r);
    tree[r].push(l);
    return tree;
  },
  Array.from({ length: n + 1 }, () => [])
);

const bfs = (start) => {
  const queue = [start];
  let head = 0;
  const ans = [start];
  const visited = Array.from({ length: n + 1 }, () => 0);
  visited[start] = 1;
  while (head < queue.length) {
    const node = queue[head];
    queue[head++];
    for (const next of tree[node].sort((a, b) => a - b)) {
      if (visited[next]) continue;
      visited[next]++;
      queue.push(next);
      ans.push(next);
    }
  }
  return ans.join(" ");
};
const dfs = (start) => {
  const stack = [start];
  const ans = [];
  const visited = Array.from({ length: n + 1 }, () => 0);
  while (stack.length > 0) {
    const node = stack.pop();
    if (visited[node]) continue;
    visited[node]++;
    ans.push(node);
    for (const next of tree[node].sort((a, b) => b - a)) {
      if (visited[next]) continue;
      stack.push(next);
    }
  }
  return ans.join(" ");
};

const ans = [dfs(v), bfs(v)];
console.log(ans.join("\n"));
