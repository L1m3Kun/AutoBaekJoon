const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const N = Number(input[0]);
const M = Number(input[1]);

const busLines = Array.from(Array(N + 1), () => []);

input.slice(2, 2 + M).forEach((el) => {
  const [s, e, c] = el.split(' ').map(Number);
  busLines[s].push([e, c]);
});

const [start, end] = input[M + 2].split(' ').map(Number);

const heapQ = [0];

const pushQ = (item) => {
  heapQ.push(item);
  let head = heapQ.length - 1;
  while (head >> 1 > 0) {
    if (heapQ[head >> 1][1] > heapQ[head][1]) {
      [heapQ[head >> 1], heapQ[head]] = [heapQ[head], heapQ[head >> 1]];
    }
    head >>= 1;
  }
};

const popQ = () => {
  const popItem = heapQ[1];
  if (heapQ.length === 2) {
    return heapQ.pop();
  }

  heapQ[1] = heapQ.pop();
  let head = 1;
  while (head < heapQ.length) {
    let node = head;
    const [left, right] = [node << 1, (node << 1) + 1];

    if (right < heapQ.length && heapQ[right][1] < heapQ[node][1]) {
      node = right;
    }
    if (left < heapQ.length && heapQ[left][1] < heapQ[node][1]) {
      node = left;
    }
    if (node === head) break;
    [heapQ[head], heapQ[node]] = [heapQ[node], heapQ[head]];
    head = node;
  }
  return popItem;
};

const cities = Array(N+1).fill(0);
cities[start] = 1;
pushQ([start, 0]);
let ans = 0;
while (heapQ.length > 0) {
  const [edge, cost] = popQ();
  cities[edge] = 1;
  if (edge === end) {
    ans = cost;
    break;
  }
  for (let [node, c] of busLines[edge]) {
    if (!cities[node]){
      pushQ([node, cost + c]);    
    }
  }
}
console.log(ans);
