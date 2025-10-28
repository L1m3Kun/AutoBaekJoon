const fs = require("fs");
const inputs = fs.readFileSync("/dev/stdin").toString().trim().split("\n");

const [n, m] = inputs[0].split(" ").map(Number);
const [sI, sJ, d] = inputs[1].split(" ").map(Number);

const direction = [
  [-1, 0],
  [0, 1],
  [1, 0],
  [0, -1],
];

const room = inputs.slice(2).map((str) => str.split(" ").map(Number));

const turn = (n) => {
  if (n - 1 >= 0) return n - 1;
  return 3;
};

const turnBack = (n) => {
  return (n + 2) % 4;
};

const isCleanAround = (i, j) => {
  for (const idx in direction) {
    const [di, dj] = direction[idx];
    const [ni, nj] = [i + di, j + dj];
    if (0 > ni || ni >= n || 0 > nj || nj >= m) continue;
    if (!room[ni][nj]) return idx;
  }
  return -1;
};

const solution = (n, m, sI, sJ, d) => {
  let clear = 0;
  let [i, j] = [sI, sJ];
  while (true) {
    if (!room[i][j]) {
      room[i][j] = 2;
      clear++;
    }

    const isC = isCleanAround(i, j);
    if (isC < 0) {
      const bIdx = turnBack(d);
      const [bi, bj] = direction[bIdx];
      const [ni, nj] = [bi + i, bj + j];
      if (0 > ni || ni >= n || 0 > nj || nj >= m || room[ni][nj] === 1)
        return clear;
      [i, j] = [ni, nj];
    } else {
      for (let a = 0; a < 4; a++) {
        d = turn(d);
        const [di, dj] = direction[d];
        const [ni, nj] = [i + di, j + dj];
        if (0 > ni || ni >= n || 0 > nj || nj >= m || room[ni][nj] > 0)
          continue;
        [i, j] = [ni, nj];
        break;
      }
    }
  }
};

const ans = solution(n, m, sI, sJ, d);
console.log(ans);

