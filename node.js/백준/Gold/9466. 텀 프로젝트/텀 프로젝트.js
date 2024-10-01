const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const T = Number(input[0]);

const isCircle = (start, arr, visited) => {
    const stack = [];
    let i = start;
    while (true){
        stack.push(i);
        visited[i] = 1;
        const node = arr[i];
        if (visited[node]) {
            if (stack.includes(node)){
                return stack.length - stack.indexOf(node);
            }
            return 0;
        }
        i = node;
    }
    return 0;
}
const answer = [];
for (let t = 1; t<=T*2; t += 2) {
    const N = Number(input[t]);
    const arr = [0];
    const v = Array(N+1).fill(0);
    input[t+1].split(' ').forEach(e => {
        arr.push(Number(e));
    });
    let ans = 0;
    for (let idx=1; idx <= N; idx++) {
        if (v[idx]) continue;
        ans += isCircle(idx, arr, v);
    }
    answer.push(N-ans);
}
console.log(answer.join('\n'));