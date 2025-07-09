const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
const stack = input.slice(1).reduce((stack, num) => {
    if (num) stack.push(num);
    else stack.pop();
    return stack;
}, []);
const ans = stack.reduce((acc, cur) => cur+acc, 0);
console.log(ans);