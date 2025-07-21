const fs = require('fs');
const inputs = fs.readFileSync('/dev/stdin').toString().trim().split("\n").map(Number);
const stack = [];
let idx = 1;
let ans = [];
for (let i = 1; i <= inputs[0] ; i++){
    stack.push(i);
    ans.push("+");

    while (stack.length > 0 && inputs[idx] === stack[stack.length-1]){
        stack.pop();
        ans.push("-");
        idx++;
    }
}
if (stack.length >= 1) {
    ans = ["NO"];
}
console.log(ans.join("\n"));