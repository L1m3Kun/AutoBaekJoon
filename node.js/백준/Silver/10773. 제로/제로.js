const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
const [_, ans] = input.slice(1).reduce(([stack, sum], num) => {
    if(num) {
        stack.push(num);
        sum += num;
    }
    else sum -= stack.pop();
    return [stack, sum]
}, [[], 0]);

console.log(ans);