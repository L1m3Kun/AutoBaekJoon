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
let minV = INF;

(() => {
  const queue = [[0,0,0]];
  let head = 0;
  const visited = new Set([]);
  while (queue.length > head) {
//  console.log(`===${head}===`)
    const [x, y, count] = queue[head];
    queue[head++] = null;
//  console.log(`x= ${x}, y= ${y}`);

    if (y === T) {
      minV = count;
      break;
    }
//  console.log("---for---")
      
    for (let range = 2; range >= -2; range --) {
        const dy = y+range;
        if (dy < 0 || dy > T) continue;
        for (const dx of sortedByY[dy]) {
            //console.log(dy, dx, dy*maxX+dx)
            if (visited.has(dy*maxX+dx)) continue;
            if (Math.abs(dx-x) > 2) continue;
            queue.push([dx, dy, count+1]);
            visited.add(dy*maxX+dx);
        }

    }
  }
})();

console.log(minV === INF ? -1 : minV)