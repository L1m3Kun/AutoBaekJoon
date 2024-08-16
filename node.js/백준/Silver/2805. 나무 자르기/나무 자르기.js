const fs = require('fs');
const input = fs.readFileSync('/dev/stdin')
                .toString()
                .trim()
                .split('\n');

const [N, M] = input[0].split(' ').map(Number);
const trees = input[1].split(' ').map(Number).sort((a,b) => a-b);

const cutting = (cutLine) => {
    let log = 0;
    for (let i = N-1; i >= 0; i--){
        if (cutLine > trees[i]) break;
        log += trees[i] - cutLine;
    }
    return log;
}

let start = 0;
let end = trees[N-1];
let ans = 0;
while (start <= end) {
    let mid = Math.floor((start+end) / 2);
    const log = cutting(mid);
    if (log >= M) {
        ans = Math.max(ans, mid)
        start = mid + 1;
    } else {
        end = mid - 1;
    }
}
console.log(ans);