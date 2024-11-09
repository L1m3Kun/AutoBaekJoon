const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const solution = (M, printerQ) => {
  let cnt = 0;
    
  const que = [...printerQ];
  printerQ.sort((a, b) => b[0] - a[0])  
  let head = 0;
  let priorityHead = 0;

  while (head < que.length) {
    const task = que[head++];
    if (task[0] >= printerQ[priorityHead][0]) {
      cnt++;
      priorityHead++;
      if (task[1] === M) break;
    } else {
      que.push([...task]);
    }
  }
  return cnt;
};

let t = 1;
const ans = [];
while (t < input.length) {
  const [_, M] = input[t++].split(" ").map(Number);
  const printerQ = input[t++].split(" ").map((e, i) => [Number(e), i]);
  ans.push(solution(M, printerQ));
}
console.log(ans.join('\n'));
