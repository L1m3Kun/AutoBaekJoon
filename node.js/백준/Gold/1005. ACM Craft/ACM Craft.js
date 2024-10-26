const fs = require("fs");
const input = fs
  .readFileSync(process.platform === "linux" ? "/dev/stdin" : "./input.txt")
  .toString()
  .trim()
  .split("\n");

const solution = (N, dueArray, costArray, W) => {
  const graph = Array.from({ length: N + 1 }, () => []);
  costArray.forEach((e) => {
    const [edge, node] = e.split(" ").map(Number);
    graph[node].push(edge);
  });
  const dp = Array.from({ length: N + 1 }, (_, i) => dueArray[i - 1]);
  const visited = Array(N + 1).fill(0);
  const crafting = (edge) => {
    let maxV = 0;
    for (let node of graph[edge]) {
      if (!visited[node]) {
        dp[node] = crafting(node);
        visited[node] = 1;
      }
      maxV = Math.max(maxV, dp[node]);
    }
    return maxV + dueArray[edge - 1];
  };

  return crafting(W);
};

let t = 1;
const ans = [];
while (t < input.length) {
  const [N, K] = input[t++].split(" ").map(Number);
  const dueArray = input[t++].split(" ").map(Number);
  const costArray = input.slice(t, t + K);
  t += K;
  const W = Number(input[t++]);
  ans.push(solution(N, dueArray, costArray, W));
}

console.log(ans.join("\n"));
