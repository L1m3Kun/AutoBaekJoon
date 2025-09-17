const fs = require("fs");
const [F, S, G, U, D] = fs
  .readFileSync("/dev/stdin")
  .toString()
  .trim()
  .split(" ")
  .map(Number);

const dfs = () => {
  const queue = [[S, 0]];
  let head = 0;
  const visited = Array.from({ length: F + 1 }, () => 0);
  let minV = 1000000;
  visited[S] = 1;
  while (queue.length > head) {
    const [floor, cnt] = queue[head];
    queue[head++] = null;

    if (floor === G) {
      minV = Math.min(minV, cnt);
      continue;
    }
    if (minV < cnt) continue;
    for (const nextFloor of [floor + U, floor - D]) {
      if (nextFloor > F || nextFloor < 1 || visited[nextFloor]) continue;
      visited[nextFloor]++;
      queue.push([nextFloor, cnt + 1]);
    }
  }
  return minV;
};

if (S > G && D === 0) console.log("use the stairs");
else if (S < G && U === 0) console.log("use the stairs");
else if (S === G) console.log(0);
else {
  const ans = dfs();
  if (ans === 1000000) {
    console.log("use the stairs");
  } else {
    console.log(ans);
  }
}
