const fs = require('fs');
const [T, ...cases] = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

const visited= {1:1, 2:2};

const solution = (t) => {
    let curr = t;
    let maxV = t;
    while ((curr & (curr-1)) !== 0){
        if (curr & 1){
            curr = curr * 3 + 1;
        } else {
            curr /= 2;
        }
        maxV = Math.max(maxV, curr);
    }
    visited[t] =  Math.max(maxV, curr);
    return visited[t];
}

const ans = cases.map(t => solution(t));
console.log(ans.join('\n'));