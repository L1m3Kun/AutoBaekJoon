const fs = require('fs');
const [N, M] = fs.readFileSync('/dev/stdin').toString().trim().split(' ').map(Number);
const ans = [];
const visited = Array(N+1).fill(0);
const stack = [];
const bf = (start) => {
    if (stack.length === M){
        ans.push(stack.join(' '));
        return;
    }
    for (let i = 1; i <= N; i++){
        if (!visited[i]) {
            visited[i] = 1;
            stack.push(i);
            bf(i);
            stack.pop();
            visited[i] = 0;
        }
    }
}

bf(1);
console.log(ans.join('\n'));