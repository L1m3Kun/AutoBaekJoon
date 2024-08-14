const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n')
                .map(e => e.split(' ').map(Number));
const main = (N, M, friendship) => {
  // codespace
  const friends = {};
  friendship.forEach(([l, r]) => {
    if (l in friends){
        friends[l].add(r);
    } else {
        friends[l] = new Set([r]);
    }
    
    if (r in friends) {
        friends[r].add(l);
    } else {
        friends[r] = new Set([l]);
    }
  });

  const ans = Array(N).fill(0);

  for (let s = 1; s<=N;s++){
    const stack = [s];
    const visited = Array(N).fill(-1);
    visited[s-1] = 0;
    while (stack.length > 0){
        const node = stack.shift();
        for (edge of [...friends[node]]) {
            if (visited[edge-1] === -1){
                visited[edge-1]= visited[node-1] + 1;
                stack.push(edge);
            }
        }
    }
    ans[s-1] = visited.reduce((prev, now) => now === -1? prev:prev+now,0);
    
  }
  let minIdx = 0;
  ans.forEach((e,i) => {
    if ( e < ans[minIdx]) minIdx = i;
  });

  return minIdx + 1;
}
console.log(main(input[0][0],input[0][1], input.slice(1)));

