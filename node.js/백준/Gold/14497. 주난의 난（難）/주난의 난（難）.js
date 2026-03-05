const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, M] = inputs[0].split(" ").map(Number);
const [x1, y1, x2, y2] = inputs[1].split(" ").map(Number).map((num) => num-1);
const classroom = inputs.slice(2);
const directions = [[1,0], [0,1], [-1,0], [0,-1]];
const field = Array.from({length: N}, () => Array(M).fill(-1));
(() => {
  const queue = [[x1,y1,0]];
  let head = 0;
  field[x1][y1] = 0;
  while(queue.length > head) {
    const [x, y, count] = queue[head];
    queue[head++] = null;
    for (const [dx, dy] of directions) {
      const [nx, ny] = [dx+x, dy+y];
      if (
        nx < 0 ||
        nx >= N ||
        ny < 0 ||
        ny >= M
      ) continue;
      if (field[nx][ny] >= 0) continue;

      field[nx][ny] = count;
      if (classroom[nx][ny] === "1" ) {
        queue.push([nx,ny, count+1]);
        continue;
      }
      
      queue[--head] = [nx,ny, count];

    }
  }
})()

console.log(field[x2][y2]+1);