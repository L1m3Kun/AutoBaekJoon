const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);
const N = input[0];
const stack = [];
let ans = 0;
input.slice(1).forEach(fan => {
    while (stack.length > 0 && fan > stack[stack.length-1][0]) {
        ans += stack.pop()[1];
    }
    if (stack.length > 0) {
        if (fan === stack[stack.length-1][0]) {
            ans += stack[stack.length-1][1]
            if (stack.length > 1) ans ++;
            stack[stack.length-1][1] ++;
        } else {
            stack.push([fan, 1]);
            ans ++;
        }
    } else {
        stack.push([fan, 1]);
    }
});
console.log(ans);