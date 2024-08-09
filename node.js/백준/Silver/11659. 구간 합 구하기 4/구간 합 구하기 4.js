const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const arr = input[1].split(' ').map(Number);
const order = input.slice(2).map(e=> e.split(' ').map(Number));

for (let i=1;i<N;i++){
    arr[i] += arr[i-1];
}
const ans = [];

order.forEach((e) => {
    if (e[0] === 1) {
        ans.push(arr[e[1]-1]);
    } else {
        ans.push(arr[e[1]-1] - arr[e[0]-2]);
    }
});
console.log(ans.join('\n'));