const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");
const [N, M] = inputs[0].split(" ").map(Number);
const [x1, y1, x2, y2] = inputs[1].split(" ").map(Number).map((num) => num-1);
const classroom = inputs.slice(2)
                        .map((l) => l.split("")
                                     .map((item) => {
                            if (item === "*" || item === "#") return item;
                            return +item;
                        }));
const directions = [[1,0], [0,1], [-1,0], [0,-1]];

const bfs = () => {
  const queue = [[x1,y1]];
  let head = 0;
  const visited = new Set([x1 * M + y1]);
  const field = classroom.map((l)=>l.slice(0));
  
  //console.log(classroom);
  while(queue.length > head) {
    const [x, y] = queue[head];
    queue[head++] = null;
    //console.log(`x=${x}, y=${y}`);
    //console.log(field);
    if (x === x2 && y === y2) return 1; 
    for (const [dx, dy] of directions) {
      const [nx, ny] = [dx+x, dy+y];
      if (
        nx < 0 ||
        nx >= N ||
        ny < 0 ||
        ny >= M
      ) continue;
      //console.log(`nx=${nx}, ny=${ny}`);
      //console.log(visited);
      if (visited.has(nx * M + ny)) continue;
      visited.add(nx * M + ny);
      if (field[nx][ny] === "#") return 1;
      if (field[nx][ny] === 1) {
        field[nx][ny] = 0;
        continue;
      }
      queue.push([nx,ny]);
    }
  }

  classroom.forEach((_, idx, arr) => {
    arr[idx] = field[idx].slice(0);
  });

  return 0;
}
let i= 0;
for (i = 1; i < 300*300+1; i++) {
  //console.log(`===${i}===`);
  const isFinish = bfs();
  if (isFinish) break;
}
console.log(i);