const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin")
                           .toString()
                           .trim()
                           .split("\n");
const [[n, T], ...halls] = inputs.map((l)=> l.split(" ").map(Number));
const INF = 50000;
let maxX = 0;
const sortedByY = halls.reduce((wall, [x,y], idx) => {
    wall[y].push(x);
    maxX = Math.max(maxX, x);
    return wall;
}, Array.from({length: T+1}, () => []))

const ans = (() => {
  const queue = [[0,0,0]];
  let head = 0;
  const visited = new Set([]);
  while (queue.length > head) {
    const [x, y, count] = queue[head];
    queue[head++] = null;

    if (y === T) {
      return count;
    }
    for (let range = 2; range >= -2; range --) {
      const dy = y+range;
      if (dy < 0 || dy > T) continue;
      for (const dx of sortedByY[dy]) {

        if (Math.abs(dx-x) > 2) continue;
        if (visited.has(dy*maxX+dx)) continue;
          queue.push([dx, dy, count+1]);
          visited.add(dy*maxX+dx);
      }
    }
  }
  return -1;
})();

console.log(ans);