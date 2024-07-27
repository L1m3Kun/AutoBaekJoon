const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
const stack = [];
let sum = 0;
input.slice(1).forEach((e) => {
    if (e) {
        stack.push(e);
        sum += e;
    } else {
        sum -= stack.pop();
    }
});

console.log(sum);