const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [V, E] = input[0].split(' ').map(Number);
const start = Number(input[1]);
const graph = Array.from(Array(V + 1), () => []);

input.slice(2).forEach((e) => {
  const [u, v, w] = e.split(' ').map(Number);
  graph[u].push([v, w]);
});

const heapQ = [0];

const pushQ = (item) => {
  heapQ.push(item);
  let idx = heapQ.length - 1;
  while (idx >> 1 > 0) {
    const parent = idx >> 1;
    if (heapQ[idx][0] < heapQ[parent][0]) {
      [heapQ[idx], heapQ[parent]] = [heapQ[parent], heapQ[idx]];
    } else {
      break;
    }
    idx >>= 1;
  }
};

const popQ = () => {
  const popItem = heapQ[1];
  if (heapQ.length === 2) {
    heapQ.pop();
    return popItem;
  }
  heapQ[1] = heapQ.pop();
  let idx = 1;
  while (idx < heapQ.length) {
    let node = idx;
    const [left, right] = [idx << 1, (idx << 1) + 1];
    if (left < heapQ.length && heapQ[left][0] < heapQ[node][0]) {
      node = left;
    }
    if (right < heapQ.length && heapQ[right][0] < heapQ[node][0]) {
      node = right;
    }
    if (node === idx) break;
    [heapQ[node], heapQ[idx]] = [heapQ[idx], heapQ[node]];
    idx = node;
  }
  return popItem;
};

const visited = Array(V + 1).fill(3000001);
visited[start] = 0;
pushQ([0, start]);

while (heapQ.length > 1) {
  const [cost, edge] = popQ();
  if (cost > visited[edge]) continue;
  for (let [node, c] of graph[edge]) {
    if (visited[node] > cost + c) {
      visited[node] = cost + c;
      pushQ([cost + c, node]);
    }
  }
}
const ans = visited.slice(1).map((e) => (e === 3000001 ? 'INF' : e));
console.log(ans.join('\n'));
