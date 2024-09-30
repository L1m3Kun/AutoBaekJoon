const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');
const [N, M] = input[0].split(' ').map(Number);
const arr = Array(N).fill(0);
input.slice(1).forEach(e => {
    const [i, j, k] = e.split(' ').map(Number);
    for (let idx = i-1; idx <j ; idx++){
        arr[idx] = k;
    }
});
console.log(arr.join(' '));