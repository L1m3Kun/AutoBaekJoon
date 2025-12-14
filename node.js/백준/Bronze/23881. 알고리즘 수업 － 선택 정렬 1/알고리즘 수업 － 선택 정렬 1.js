const fs = require('fs');
const inputs = fs.readFileSync('/dev/stdin').toString().trim().split("\n");
const [N, K] = inputs[0].split(" ").map(Number);
const A = inputs[1].split(" ").map(Number);

const selectionSort = (arr) => {
    let k = 0;
    for (let last = N; last > 0 ; last--) {
        const maxIdx = arr.slice(0, last).reduce((res, num, i, origin)=>origin[res] < num ? i : res , 0);
        if (maxIdx !== last - 1) {
            [arr[maxIdx], arr[last-1]] = [arr[last-1], arr[maxIdx]];
            k ++;
            if (k === K) return [arr[maxIdx], arr[last-1]].join(" ");
        }
    }
    return -1;
}

console.log(selectionSort(A));