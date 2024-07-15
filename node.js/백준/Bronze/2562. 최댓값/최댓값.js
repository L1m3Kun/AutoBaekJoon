const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split('\n').map(Number);

let ans = [input[0],1];

input.forEach((e,i) => {
    if (ans[0] < e){
        ans[0] = e
        ans[1] = i+1
    }
})
console.log(ans.join('\n'));